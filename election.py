#implement five functions

#---------

#implementing sample list to be counted

parties = ['party1','party2','party3']

#count_parties

#parameter is that parties is already a defined list

def count_parties(parties):
    #counts the number of parties in a list called "parties"

    count = len(parties)
    
    return count

    #returns the newly defined variable "count"

#counts the elements in a list

#---------

#count_votes
    
#parameters:
    #parties is a defined list of party names
    #votes is a list of all the parties that were votes for
    
parties = ['A','B','C']
votes = ['A','A','C','A','C']

def count_votes(parties,votes):
    
    #create a lists that holds the number of votes for each party
    
    list1 = []
    for i in range(len(parties)):
        list1.append(0)
    
    #iterate through list of votes (number of parties) times
    
    for i in range(len(parties)):
        for v in range(len(votes)):
            if votes[v] == parties[i]:
                list1[i] = list1[i] + 1
                
    #define list1
                
    return list1    

#counts the votes recieved by each party

#---------

#first_choices

#define parameters
#parties must be a list of parties

parties = ['party1','party2','party3']

#ballots is a list of lists

b1 = ['party1','party2','party3']

b2 = ['party2','party1','party3']

b3 = ['party3','party2','party1']
b4 = ['party1','party2','party3']
b5 = ['party3','party1','party2']

ballots = [b1,b2,b3,b4,b5]

def first_choices(parties,ballots):
    #iterate through every list contained in the list "ballots"
    #check the first index
    
    #create a list with sufficient indexes
    list2 = []
    for i in range(len(parties)):
        list2.append(0)
    
    #must check the first index in the ballot (number of parties) times
    for p in range(len(parties)):
        
        for i in range(len(ballots)):
            if (ballots[i])[0] == parties[p]:
                list2[p] = list2[p] + 1
            
    #return the newly defined list
    
    return list2

    pass

    #((ballots[0])[0]) checks the first index of the list in the first index

#counts the first-choice votes for each party in a ranked voting system
    

#---------

#remove

#define parameters
#haystack is a iterable list
haystack = ['needle','one','two','haystack','three']

def remove(needle,haystack):
    
    haystack = list(haystack)
    
    for i in range(len(haystack)):
        
        #ensures that code won't run when i surpasses the indexes available in the list
        #since removing an index will cause the list to shorten
        
        if i<len(haystack):
            
            if haystack[i] == needle:
                haystack.remove(needle)
            
    
    return haystack

#removes a less preferred party from a list

#---------

#ranked_ballot

#parameters:
#parties, list of parties
#ballots, list of ballots which are individual lists of parties

def ranked_ballot(parties,ballots):
    
    #create a loop that can be broken
    
    decision = False
    while decision == False:
    
    #create a list that displays all the top votes for the parties
        
        list2 = first_choices(parties,ballots)
        if max(list2) > sum(list2) - max(list2):
            
            decision = True
           #determine the index of the greatest value and print the corresponding party name
            winner = parties[list2.index(max(list2))]
    
        else:
            loser = parties[list2.index(min(list2))]
            for i in range(len(ballots)):
                remove(loser,ballots[i])
            
    winner = parties[list2.index(max(list2))]
    return winner

#counts the number of votes for each party
#checks if greatest number of votes recieved more than half
#removes the loser from each ballot

#counts number of votes again
#removes loser

#one party remains, this is the winnner

#preforms a ranked-ballot election



