num_tickets = 8

tickets_requested = int(raw_input("How many tickets would you like? "))

print "You've asked for {} ticket(s)".format(tickets_requested)

if tickets_requested > num_tickets:
  print "You've requested too many tickets!"
elif tickets_requested == num_tickets:
  print "You've requested all of the tickets!"
else:
  num_tickets = num_tickets - tickets_requested
  print "There are {} ticket(s) left.".format(num_tickets)
