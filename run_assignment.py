
people = ["Colette", "Todd", "Erin", "Chris", "Meghan", "Jason", "Taryne",
  "Jeff", "Grayson", "Julie", "Toni", "Tim", "Sarah", "Michael"]

BadPairs = set()

print people

def bad(*group):
  for person1 in group:
    assert(person1 in people)
    for person2 in group:
      assert(person2 in people)
      BadPairs.add( (person1, person2 ) )

def addYear(yearString):
  for line in yearString.strip().split("\n"):
    print line
    pair = line.split("\t")
    print "pair:", pair
    pairTup = (pair[0].strip(), pair[1].strip())
    assert(pairTup[0] in people)
    assert(pairTup[1] in people)
    BadPairs.add(pairTup)

bad("Colette", "Todd")
bad("Erin", "Chris")
bad("Meghan", "Jason")
bad("Taryne", "Jeff")
bad("Grayson", "Julie")
bad("Toni", "Tim", "Sarah", "Michael")

y2013 = """
Todd	Tim
Colette	Todd
Meghan	Toni
Erin	Sarah
Taryne	Colette
Grayson	Meghan
Tim	Taryne
Toni	Chris
Sarah	Grayson
Chris	Erin
"""

y2014 = """
Todd	Toni
Colette	Sarah
Meghan	Colette
Erin	Meghan
Taryne	Tim
Grayson	Erin
Tim	Todd
Toni	Grayson
Sarah	Taryne
Chris	Michael
Michael	Chris
"""

y2015 = """
Todd	Sarah
Colette	Toni
Meghan	Michael
Erin	Tim
Taryne	Grayson
Grayson	Chris
Tim	Colette
Toni	Meghan
Sarah	Erin
Chris	Todd
Michael	Taryne
"""

y2016 = """
Todd	Colette
Colette	Tim
Meghan	Sarah
Erin	Todd
Taryne	Julie
Grayson	Michael
Tim	Meghan
Toni	Taryne
Sarah	Chris
Chris	Erin
Michael	Grayson
Julie	Toni
"""

y2017 = """
Grayson	Tim
Julie	Chris
Taryne	Erin
Meghan	Grayson
Jeff	Michael
Sarah	Julie
Jason	Toni
Chris	Sarah
Tim	Jeff
Erin	Jason
Toni	Colette
Colette	Taryne
Todd	Meghan
Michael	Todd
"""

addYear(y2013)
addYear(y2014)
addYear(y2015)
addYear(y2016)
addYear(y2017)

print BadPairs

def explore(assignment, givers, index, receiversLeft):
  if len(receiversLeft) == 0:
    print "assignment is", assignment, "\n\n"
    return
  if True:
    giver = givers[index]
    for receiver in receiversLeft.copy():
      pair = (giver, receiver)
      if pair in BadPairs:
        continue
      revPair = (pair[1], pair[0])
      BadPairs.add(revPair)
      receiversLeft.remove(receiver)
      explore(assignment + [pair], givers, index+1, receiversLeft)
      receiversLeft.add(receiver)
      BadPairs.remove(revPair)

def exploreBackup(assignment, giversLeft, receiversLeft, depth=1):
  print "entering explore"
  if len(giversLeft) == 0:
    print "assignment is", assignment
    return
  for giver in giversLeft.copy():
    giversLeft.remove(giver)
    for receiver in receiversLeft.copy():
      pair = (giver, receiver)
      if pair in BadPairs:
        continue
      revPair = (pair[1], pair[0])
      BadPairs.add(revPair)
      receiversLeft.remove(receiver)
      explore(assignment + [pair], giversLeft, receiversLeft)
      receiversLeft.add(receiver)
      BadPairs.remove(revPair)
    giversLeft.add(giver)


if __name__ == "__main__":
  explore([], list(people), 0, set(people))

      
