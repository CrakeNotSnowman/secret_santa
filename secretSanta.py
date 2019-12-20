



from random import shuffle
try:
    import kmmessage
except ImportError:
    print("kmmesage module not found. No emails will be sent")
    kmmessage = False

'''
Author: Keith Murray 
email: kmurrayis@gmail.com


This is a really simple secret santa assignment script
which emails each person the name of the person they're 
getting a gift for. 

It needs dictionary of name:email key value pairs as input, 
and has an optional 'couples' input which will force the 
program to re-roll if any couple is buying a gift for their
significant other. 

The couples input should be a list of lists, where the interior
list is populated with the names (keys) of the memembers of 
the couple. It isn't limited to two, so you can have larger sets
of people which don't get a gift for each other.

The couple exclusion isn't written well, but it's functional so
unless I'm bored it'll probably stay as it is.


'''


def shiftit(names, i):
    '''
    Following the method laid out by Dr Hannah Fry in 
    a Numberphile video: 
    https://www.youtube.com/watch?v=5kC5k5QBqcc
    and with some modifications: 
    after a shuffle, each person gets a gift for the person 
    to their right in the list
    '''
    i += 1
    if i == len(names):
        i = 0
    return names[i]

def couple_gift(names, couples):
    '''
    Looks to see if a member of a couple 
    is buy a gift for their partner
    '''
    #couples = [['a', 'b'], ['c', 'd']]
    for i in range(len(names)):
        a = names[i]
        b = shiftit(names, i)
        for couple in couples:
            if (a in couple) and (b in couple):
                return False
    return True


def make_assignments(emails, couples=[], send_email=True):
    '''
    The secret santa assignment
    '''
    names = list(emails.keys())

    for couple in couples:
        for person in couple:
            assert person in emails, "Person "+person+" Does not have an associated email"

    no_couples = False
    while not no_couples:
        shuffle(names)
        no_couples = couple_gift(names, couples)

    for i in range(len(names)):
        msg = names[i].capitalize() + ' you are buying a gift for ' + shiftit(names, i).capitalize() + '\nMerry Christmas!'
        addr = emails[names[i]]
        # Build Email
        subj = "Secret Santa"
        if send_email and kmmessage:
            kmmessage.message_Send_Full_Email([addr], subj, msg)
        else:
            #print('*'*10)
            #print('To:   '+addr)
            #print('Subj: '+subj)
            print(msg)
    return


def demo():
    sample_emails = {'a':'a@example.com',
                     'b':'b@example.com',
                     'c':'c@example.com',
                     'd':'d@example.com',
                     'e':'e@example.com',
                     'f':'f@example.com'}
    sample_couples = [['a', 'b'], ['c', 'd']]

    make_assignments(sample_emails, couples=sample_couples, send_email=False)
    return