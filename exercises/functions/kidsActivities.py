
# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take varying number of children's names as the argument.
'''
For example, the run function would be defined as follows:

def run(*kids):
    # Loop through all the kids and print that the child performed the activity.

run("Joe", "Jenna")
# Output: 
# "Joe ran like a fool!"
# "Jenna ran like a fool!"
Do the same for the following children:

Running kids: Pam, Sam, Andrea, Will
Swinging kids: Marybeth, Ariel, Kevin, Courtney
Sliding kids: Mike, Jack, Jennifer, Earl
Hiding kids: Henry, Heather, Hayley, Hugh

'''

def running(*kids):
    for name in kids:
        print(f'{name} ran like a fool!')

def swinging(*kids):
    for name in kids:
        print(f'{name} was just a swinging!')

def sliding(*kids):
    for name in kids:
        print(f'{name} sliding into home!')

def hiding(*kids):
    for name in kids:
        print(f'{name} was playing hide and seek!')

running("Gavin", "Gunnar", "Grayson")
running("Pam", "Sam", "Andrea", "Will")
swinging("Marybeth", "Ariel", "Kevin", "Courtney")
sliding("Mike", "Jack", "Jennifer", "Earl")
hiding("Henry", "Heather", "Hayley", "Hugh")






