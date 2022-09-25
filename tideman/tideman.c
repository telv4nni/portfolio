#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
int check_cycle(int winner, int loser);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

           if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < (candidate_count - 1); i++)
    {
        for (int j = 1; j < candidate_count; j++)
        {
            if (ranks[i] != ranks[j])
            {
                preferences[ranks[i]][ranks[j]]++;
            }
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i] && (i != j))
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
        }
    }

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        for (int j = i; j < pair_count; j++)
        {
            //if ((pairs[i].winner - pairs[i].loser) < (pairs[j].winner - pairs[j].loser))
            if ((preferences[pairs[i].winner][pairs[i].loser]) < (preferences[pairs[j].winner][pairs[j].loser]))
            {
                int winner;
                int loser;
                winner = pairs[i].winner;
                loser = pairs[i].loser;
                pairs[i].winner = pairs[j].winner;
                pairs[i].loser = pairs[j].loser;
                pairs[j].winner = winner;
                pairs[j].loser = loser;
            }
        }
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        //check if cycle exist, return true if not
        if (check_cycle(pairs[i].winner, pairs[i].loser) == 0 && locked[pairs[i].loser][pairs[i].winner] != true)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}
int check_cycle(int winner, int loser)
{
    for (int i = 0; i < pair_count; i++)
    {
    //check if the loser of pair already have an arrow towards someone else
    if (locked[loser][i] == true)
        {
            //check if there's an arrow towards winner
            if (locked[i][winner] == true)
            {
                return 1;
            }
            //check another pair if there's an arrow towards winner
            check_cycle(winner, i);
        }
    }
    return 0;
}
// Print the winner of the election
void print_winner(void)
{
    printf("%s\n", candidates[pairs[0].winner]);
    return;
}