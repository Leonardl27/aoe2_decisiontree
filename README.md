# aoe2_decisiontree
Decision tree planning
Create a list of various civs by categories. archer_plus, archer_minus, knight, camel, infantry
Create a list of civs by units fully upgraded. 
Create various top 3 unit list for each civ.
Create late game 2 trash 1 gold comp for each civ.

# Focus on 4 civs to start
2 knight civ's: Franks, berbers
2 archer civ's: Britons, ethiopians

# Conventions for code
use underscores to separate words
no capitalizations, use underscores, use full words. ex: thumb_ring, ballistics, elite_skirmisher

Unit lines to focus on
Scout, knight, camel, archer, skirmisher, spear
Siege to focus on
magonel, onager, siege_onager. bombardcanon, siege_engineers


## Main point of emphasis, the actual decision tree @Levi
All of the above will be good for establishing arbitrary values but here is where the magic will happen
We need to create a program that will create different scenarios for battle setups. Judging from all of the
unit bonuses and we can imagine a big battle on an open map like arabia. Then we can asign values to how well we like this matchups.

# For example
Franks vrs. Britons. We're Britons
Frank Palidan, skirm, treb vrs Briton Arb, scout_cav, pikeman: Maybe we assign a frank win percentage of 70%  -5 value
Frank Palidan, skimisher, treb vrs Britons Arb, pikeman, onager: Assign britons win percentage of 60%  +3 Value

Obviously there is a ton a variability, but I feel like it happens in enough games where we run up against weird 
civs and with our civ we're not sure what our ideal setup is. So if we can assign preffered values to all of these matchups
we have at least some idea of where to go with units to make. Even poll members of the group. I've have a few ideas, 
just not sure how to execute them.
