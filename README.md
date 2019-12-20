
# Secret Santa Assignments

This is a really simple secret santa assignment script
which emails each person the name of the person they're 
getting a gift for. 

It needs dictionary of name:email key value pairs as input, 
and has an optional 'couples' input which will force the 
program to re-roll if any couple is buying a gift for their
significant other. 

It's not the best code in the world, but it was written in 
about 20 minutes before I had to head out and it got the job
done. I figure it might be useful next year so it's worth holding
onto. 

### Usage

To run the program, you need to call `make_assignments` and provide it
with a dictionary. The dictionary should be built with 'name':'email' 
pairs, like

    
    sample_emails = {'a':'a@example.com',
                     'b':'b@example.com',
                     'c':'c@example.com',
                     'd':'d@example.com',
                     'e':'e@example.com',
                     'f':'f@example.com'}

Then to run call `secretSanta.make_assignments(sample_emails)`

If you have couples and want to make sure no person buys a gift for their 
significant other, or that a specific group don't buy gifts for each other
(for example memembers of a family), you can include a list of couples, where a couple is a 
list of the members (their names must be used in the emails dictionary as keys): 

    sample_couples = [['a', 'b'], ['c', 'd']]

And pass that in as well, 

    secretSanta.make_assignments(sample_emails, couples=sample_couples)

To just view results rather than emailing and make sure the program is 
opperating as expected, set `send_emails = False` and it'll print
out the email message instead of sending it.

    secretSanta.make_assignments(sample_emails, couples=sample_couples, send_email=False)


#### To send the emails

The program uses ['kmmessage'](https://github.com/CrakeNotSnowman/Python_Message)
to send emails. kmmessage is a personal library I use to handle any messaging I need
but the key componets to send the emails are built from the [smtplib](https://docs.python.org/3/library/smtplib.html) and [email](https://docs.python.org/3/library/email.html#module-email), so if you don't want to setup kmmessage, you can probably get around it using that.

A good example can be [found here](https://docs.python.org/3/library/email.examples.html)
