import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        #create sharelist
        shares = db.execute("SELECT symbol,SUM(shares), currentprice, SUM(currentprice*shares) FROM shares WHERE user_id = ? GROUP BY symbol", session["user_id"])
        #check user cash
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash[0]['cash']
        #check share prices
        for share in shares:
            price = lookup(share['symbol'])
            db.execute("UPDATE shares SET currentprice = ? WHERE user_id = ? AND symbol = ?", price['price'], session["user_id"], share['symbol'])
        return render_template("index.html", shares=shares, cash=cash)
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    """Buy shares of stock"""
    if request.method == "POST":
        ##check symbol input
        symbol = request.form.get("symbol")
        if symbol:
            price = lookup(symbol)
        if price is None:
            return apology("Incorrect symbol")
        ##check shares input
        symbol = symbol.upper()
        shares = request.form.get("shares")
        if not shares:
            return apology("Must provide shares")
        elif int(shares) <= 0:
            return apology("Shares must be positive value")

        #  Buy shares
        #Select users cash
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash[0]['cash'] - (price['price']*int(shares))
        #check if user has enough money
        if cash < 0:
            return apology("User does not have enough money")
        #update users money
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])
        #Add shares to the user
        db.execute("INSERT INTO shares (user_id, symbol, shares, price) VALUES(?,?,?,?)", session["user_id"], symbol, shares , price['price'])
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        history = db.execute("SELECT symbol, shares, price, date FROM shares where user_id = ? ORDER BY date", session)
        return render_template("history.html")
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    if request.method == "POST":
        symbol = request.form.get("symbol")
    if symbol:
            price = lookup(symbol)
    if price is None:
        return apology("incorrect symbol")
    return render_template("quoted.html", price=price)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # get user inputs and check validity
    if request.method == "GET":
            return render_template("register.html")
    if request.method == "POST":
        username = request.form.get('username')
        if not username:
            return apology("Username is missing")
        password = request.form.get("password")
        if not password:
            return apology("Password is missing")
        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("Password is missing")
        if password != confirmation:
            return apology("Passwords do not match")
    #generate password hash
    hash = generate_password_hash(password)
    #add username and hash to database
    db.execute("INSERT INTO users (username, hash) VALUES(?,?)", username, hash)
    return redirect("/")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        symbols = db.execute("SELECT symbol FROM shares WHERE user_id = ? GROUP BY symbol", session["user_id"])
        return render_template("sell.html", symbols=symbols)
    """Sell shares of stock"""
    if request.method == "POST":
        # Check if user selected a stock symbol and does have a share in that stock
        symbol = request.form.get("symbol")
        symbols = db.execute("SELECT symbol FROM shares WHERE user_id = ? GROUP BY symbol", session["user_id"])
        symbols_list = [item['symbol'] for item in symbols]
        if not symbol:
            return apology("Haven't selected a symbol")
        if symbol not in symbols_list:
            return apology("User doesn't own any share of this stock")
        # Check if user selected correct amount of shares
        sharesdb = db.execute("SELECT ?, SUM(shares) FROM shares WHERE user_id = ? GROUP BY symbol", symbol, session["user_id"])
        shares = request.form.get("shares")
        # if not isinstance(shares, int) or int(shares) <= 0:
        #     return apology("Number is not a positive integer")
        if int(shares) > int(sharesdb[0]["SUM(shares)"]):
            return apology("User does not have that many shares")
        # Sell shares
        # Update user money
        price = lookup(symbol)
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", price['price'], session["user_id"])
        # Update user shares
        db.execute("INSERT INTO shares (user_id, symbol, shares, price) VALUES(?,?,-?,?)", session["user_id"], symbol, shares, price['price'])
        return redirect("/")
