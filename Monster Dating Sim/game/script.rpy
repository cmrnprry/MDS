# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    #characters
    #Character Main Locations
    # Banshee - Club Room
    # Zombie - Stairs
    # Skeleton - Gym
    # Wendigo - Bleachers
    define banshee = Character(_("Banshee"), color = "#1ff4ff")
    define zombie = Character(_("Zombie"), color ="#2ec414")
    define sk = Character(_("Skeleton"), color ="#f7e9f5")
    define wendigo = Character(_("Wendigo"), color ="#e6152a")
    define teacher = Character(_("Teacher"), color ="#ae15e6")
    define mc = Character(_("[main]"), color ="#d6d6d6")

    #days
    $ day = 1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    python:
        main = renpy.input("What is your name?")
        main = main.strip()

        if not main:
             main = "Fergie"

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc
    # These display lines of dialogue.
    mc "First day at monster school!"
    mc "Yeah, monster school. Hopefully I don’t die."
    mc "This witch costume is just barely convincing enough, and if I get caught being a human, it could mean the end of me."
    jump classroom_day_one

#The scenes for day one
label classroom_day_one:
    scene classroom 

    show main character at left

    mc "So far, I've gone relatively unnoticed. I'm only here because I met some cool people from this school last year, and I can't go back to my assigned high school"

    mc "I spent the last year training to become a master at magicry, since after I was admitted here, I found out that you needed to be a 'monster' to attend"

    mc "I figured my best bet was to become a witch! I immediately bought the Criss Angel MINDFREAK Professional Magic Kit, and that has been the source of my tricks."

    mc "I tried to upgrade to the Penn and Teller kit, but I couldn't get it from Amazon in time"

    hide main character

    show Teacher at middle 

    snake "Sssssso classsss"

    teacher "Excuse me! Do not address my students, that is my job."

    "The teacher slaps a snake that was going towards her neck away"

    teacher "Anyways, we have a new student here today, a Witch named [mc]"

    mc "I can hear some people start questioning what type of magic I can do"

    mc "This is what I have been training for"

    teacher "Quiet down! Be nice to our new student! They came a long way to get here"

    teacher "But I might agree with the class, I would love to see a trick"

    hide Teacher

    show main character at left

    mc "Oh boy!"

    menu:
        "Pull a quarter out of a zombie's ear":
            jump perform_quater
        "Make a vase levitate":
            jump perform_levitate
        "Ask a skeleton to pick a card":
            jump perform_card

label perform_quarter:
    "I've been hiding this quarter in my sleeve for this exact moment!"

    "I show the class my empty hand, and in one swift motion I lean take a quarter out of the zombie sitting next to me decaying ear"

    "The class does not look too terribly impressed"

    jump classroom_day_one_s2

label perform_levitate:
    "I take out a small vase, bearing the Criss Angel logo."

    "I put on a small act where I act like the vase is terribly heavy for a moment, then when the audience is least expecting it, I start making it levitate!"

    "I can tell everyone has their doubts, but look fairly impressed."

    "Expect for this humanoid deer thing, who seems they will never be impressed by anything ever"

    jump classroom_day_one_s2

label perform_card:
    "I ask the closest person to me to pick a card out of my special Criss Angel deck, and tell them to show the class"

    "Knowing that it was a fool deck, I proudly announce that the card he had was an Ace of Hearts"

    "I don't notice any expression but his, which looks like a child who was just told they can have ice cream for dinner "

    jump classroom_day_one_s2

label classroom_day_one_s2:
    hide main character
    
    show teacher at middle

    teacher "Thank you for … that."
    
    snake "That sssucked"
    
    teacher "That's enough!"
    
    "The teacher puts her hair in a ponytail while the snakes hiss violently"
    teacher "It'll probably be good for us to all introduce ourselves"

    "The class audibly groans in anger, and it's comforting to know that even monsters hate ice-breakers"

    "In response, the teacher's snake growl, which I did not know was possible until this exact moment"

    teacher "Class Enough!"

    teacher "You know the sorrow of teenagers scare them!"

    "Everyone is keeping their head down, and I figure it is for good reason"
    teacher "Now, let's start introductions. Cal, go first"

    hide teacher

    show cal at middle 

    sk "Hey dude! The name's Cal."

    "He tries to put his hand out to shake mine, but he is too far away and tries to act like it never happened by stroking his hair back, even though he has none. "

    "The class does not know to go in order horizontally or vertically and it is cause major social awkwardness for everyone"

    "Someone, please go."

    hide cal

    show wendigo at middle 

    wendigo "Hi, I'm Todd Howard, but you might know me from my instagram ImWendigoingVegan."

    "I do not, but I'm slightly terrified to tell him that"

    hide wendigo 

    show banshee at middle

    banshee "HI!"

    "Some cover their ears, and the teacher motions to lower their voice"

    banshee "Sorry, I forgot how loud I can be, but my name is [INSERT NAME]"

    "The sheer volume of them trying to talk normal is more than the loudest sound i've ever heard one creature make, which, for the record, was the girl next to me at a One Direction Concert"

    hide banshee

    show zombie 

    zombie "Hello..."

    "A moment goes by"

    hide zombie 

    show teacher

    teacher "Excuse me, it would be nice to say your name"

    hide teacher

    show zombie 

    zombie "I was getting to that"

    zombie "My name is Zoë"

    "I think the teacher understands that's all she will get out of Zoe"

    hide zombie

    show teacher

    teacher "Thank you everyone, that was only half as painful to watch as last time."

    teacher "I think it's about time you all see yourselves off."

    teacher "[main], you can see yourself to wherever feels right for you, and I'm sure you'll see some of your classmates wherever you chose." 

    scene school_map

    "It seems like where I chose to go will be pretty important, so I should be sure in my choice before I go"
    menu:
        "Where do I go?"
        "To the gym":
            jump gym_day_one
        "To the hallways":
            jump behind_stairs_day_one

#Skeleton Day 1
label gym_day_one:
    scene gym
    show mc at left
    "I walk into the school's large gym. There's also a small gym but that's just a card board box where mandrakes and others play their own sports. The large gym has some equipment for everyone. I see a rather beefy…"

    "No wait, that doesn't make sense"

    show skeleton at right
    "Boney–"
    "boy, doing squats"
    mc "Hey, bro. How's it going."
    sk "Ah you know, making gains"
    mc "Bone gains?"
    sk "Hell yeah, I'm working those feems!"
    mc "Feems?"
    sk "You know, femurs."
    mc "Oh yeah, of course."
    sk "So your the new kid. A witch right?"
    mc "Yeah, that's right, I'm a witch. Got the hat, got the cat. And let me take this mat."
    "The skeleton continues doing squats."
    "Somehow"
    sk "So what are you doing?"
    mc "What am I doing?"
    sk "Yeah, like what are you working?"
    mc "You know, exercises"
    sk "What kind?"
    mc "Witch, uh, exercises"
    mc "Witch exercises" 
    mc "Magic and what not"
    sk "WOAH BRO, that shit's tight. Could you show me one?"
    mc "Yeah, sure. You want to see a spell?"
    sk "YUS, I LOVE MAGIC."
    sk "There was this motivational speaker from London or some shit, he had like a wand and made books float. Coolest day ever."
    sk "So what are you gonna do"
    mc "Uh, I have these {i}Rings of{/i}..."
    mc "{i}Rings of Cincinnati{/i}"
    "Cincinnati? Really [main]? I thought I didn't want to die."
    "I wonder what cruel, grotesque, soul crushing, way this skeleton could make me no more."
    "Oh no he's looking mad"
    sk "{i}Cincinnati{/i}?"
    sk "Sounds like an old guru. Cincinnati. Even saying it makes me feel more magical."
    sk "Awesome bro"  
    mc "Ha, yeah, he's quite the famous warlock"
    "As I reach into my pocket to pull out the rings I really hope the next class isn't geography"
    mc "Here they are {i}the Rings of Cincinnati{/i}. Behold, two interlocking rings."
    mc "However, when I say the magic words." 
    mc "{i}Toledo{/i}."
    mc "The rings merge through each other and separate." 
    sk "WOAH, how the fucking fuck?"
    mc "Magic my man"
    mc "And with the incantation:"
    mc "{i}Cleveland{/i}."
    mc "The rings re-connect. As if they were never apart."
    sk "Woah woah. Damn you really are a witch"
    show banshee
    banshee "Hey Cal, mind if I use the treadmill"
    sk "Yeah of course, it's already set up to the \"Humans running from a great evil\" path."
    banshee "Perfect"
    "While the skeleton is distracted I switch the rings with a hole with the actually connected ones"
    hide banshee
    mc "Hey do you want to try?"
    sk "Hell yeah"
    mc "Okay, be careful, these are very old relics"
    sk "Oh, they're heavy"
    "They are plastic"
    sk "Okay, here I go"
    sk "{i}Toledo{/i}"
    sk "HNNNG"
    "The skeleton pulls with so much might, yet the plastic rings don't even bend."
    sk "Damn, it isn't working. What's going wrong?"
    menu:
        mc "Well from my wisdom"
        
        "You don't have the magic touch":
            jump gym_day_one_magic

        "I don't think your strong enough":
            jump gym_day_one_strength

label gym_day_one_magic:
    sk "The magic touch?"
    jump gym_day_one_good

label gym_day_one_strength:
    sk "What's that supposed to mean?"
    mc "Well, the rings don't pop through each other effortlessly, there's some resistance"
    sk "And me, Cal. C. Um, I don't have enough strength to do this?" 
    menu:
        "Well, in all due respect"
        "How the hell do you even move?": 
            jump gym_day_one_bones
        "You don't have the right technique":
            sk "The right technique?"
            jump gym_day_one_tech

label gym_day_one_tech:
    jump gym_day_one_good

label gym_day_one_good:
    mc "Listen, I've been training my abilities for years now. You shouldn't feel bad that you aren't able to do something the first time. Persistence my boney friend."
    mc "That's why I came to the gym. To practice my spells"
    sk "Ah, spells reps"
    mc "Exactly"
    mc "Anything can happen if you try hard enough"
    sk "Yeah"
    sk "You know, I've been coming in here every morning and doing my squats. My legs don't get any bigger."
    sk "I was starting to think that my whole life was a great folly."
    sk "That I had no will, my life was already plotted by the fates."
    sk "Perhaps bones don't grow"
    sk "That it all meant nothing."
    sk "Everything"
    sk "Nothing"
    sk "However,"
    sk "YOU SHOWED ME OTHERWISE"
    sk "NOW I FEEL HYPED"
    sk "THANKS WITCH FRIEND"
    sk "HIGH FIVE"
    "I high five the skeleton's hand. The exposed bone cold on my palm"
    jump classroom_day_two


label gym_day_one_bones:
    sk "What the fuck is that supposed to mean?"
    mc "Well like, I have muscles… and you"
    mc "You don't"
    sk "You can move without muscles"
    mc "But like, you can't"
    sk "Fuck man how many times do I have to explain this?"
    sk "You know like a tinker toy? The things you wind up with a key?"
    mc "Yeah, sure"
    sk "So yeah, I get kind of winded up in the morning through messengers of hell. And then cartilage and telephaphy do the rest."
    mc "Oh okay"
    menu:
        mc "One more question"
        "Why are you exercising?":
            jump gym_day_one_bad
        "How are you so swol?":
            jump gym_day_one_okay

label gym_day_one_okay:
    sk "Ha, practice and patience"
    sk "And a bit of those handsome genes"
    sk "You like my legs?"
    mc "Yeah, they look good"
    sk "Chill, chill. Cool"
    mc "Yeah man, yeah"
    jump classroom_day_two

label gym_day_one_bad:
    sk "To get fit"
    mc "But you exercise muscles, not bones."
    sk "Man, what the fuck?"
    sk "What do you think instead of putting in the work I should, I don't know, take a milk bath?"
    mc "Yeah, maybe"
    sk "I know your a witch."
    sk "But to me all you are is a bitch."
    sk "I don't want to see anymore of your bitch magic"
    jump classroom_day_two      

#Zombie Day 1
label behind_stairs_day_one:

    scene hallway

    "While walking to my next class I noticed a girl sitting behind the stairwell. Although everyone else was hurrying to their next class, she did not make any motion to move. her nose was buried in a book that read 'Neuroscience for Dummies!'."

    show zombie at right
    show mc at left

    mc "Hey you're going to be late for class."

    "She glanced up at me and mumbled something before returning to her book."

    mc "I didn't quite catch that."

    zombie "Don't make me bite you."

    mc "Hahahahahaa. You can't turn a Witch"

    "I faked a laugh, hoping that she wouldn't. It would really suck to leave home human and return as one of the undead."

    "She glanced up at me glaring, and pushed her face further into her book."

    "I gulp and quickly pull out a trick from my magic bag."

    menu: 
        "Pull a quarter out from behind her ear":
            jump pull_quarter_zd1
        "Make a card float in mid air.":
            jump float_card_zd1
        "Sit beside her and start playing with cards.":
            jump play_card_zd1

label play_card_zd1: 
    "I sat beside her and started shuffling a Criss Angel brand deck of cards. After a few moments of fancy shuffling, she looked over and fanned out the cards in front of her."

    mc "Pick a card, any card!"

    zombie "Why?"

    mc "I'm going to read your mind! Pick a card, but don't tell me which one you pick."

    "She picked a card, glanced at it and then put it back in the deck. I did some more fancy shuffling and pulled out a card."

    mc "Iiissss this your card?"

    zombie "No."

    mc "Uh- I- What?"

    "I looked at the card in my hands and back at her. I started laughing, trying to play it off."

    mc "Of course it's not! I was just testing to make sure you were paying attention. Hahahahah."

    show zombie_sus at right

    zombie "Uh huh…"

    "I pulled another card from the deck."

    mc "Of course your card was the ace of Hearts!"

    "She nodded and looked closer at the card"

    jump end_day1_zcriss

label float_card_zd1:
    mc "Behold my Witch-y powers!"
    
    "I announced and made a card float between my hands."

    "She glanced up and looked unimpressed."

    zombie "Can you levitate anything that isn't a card?"

    mc "I- Ah- Well you see-"

    "I quickly fumble in my bag and pull out a vase and wand with the Criss Angel name and logo printed on the front."

    mc "Watch in amazement as I raise this vase into the air!"

    "I wave the plastic wand around as the vase levitates a few feet off the ground."
        
    "She squints at the logo on the vase."

    jump end_day1_zcriss

label end_day1_zcriss:

    zombie "Who is this… Criss Angel?"

    mc "He is a very famous magi- ah Witch! Yes! Very powerful and popular in the Witch community. Very very popular, don't know how you've never heard of him. Hahahahha"

    "I quickly gathered my things and started up the stairs before she could ask more questions."

    mc "I'll see you around!"

    $ zombie_sus += 10

    jump end_day_one

label pull_quarter_zd1:
    
    mc "What's that behind your ear?"
    
    "I lean over and pretend to pull a quarter from behind her ear."

    zombie "What did you-"

    "She touched behind her ear."

    show zombie_anger at right

    zombie "Why did you touch me?"

    mc "I- It's part of the spectacle!"

    show zombie_sus at right
    
    zombie "Spectacle?"

    mc "Yes! Spectacle! The best part of being a Witch is making a show of the magic."

    zombie "Riiiiggghhhttt."
    
    mc "Zombies don't make a show of, uh, eating… people..?"

    show zombie_angry at right
    
    zombie "No, we don't. We just kill and eat humans and are done with it. There's nothing \"showy\" about it"

    zombie "It is fun to chase and terrify humans but we don't make a show of it. It's just what we do."

    "She gathered her things and walked away in a huff."

    mc "Well that didn't go very well…"

    $ zombie_sus -= 10
    jump end_day_one

label end_day_one:
    $ day += 1

    mc "Well today was interesting…"

    mc "I thought my first day at Creature Academy would go a lot different, but everyone seems very nice."
        
    mc "And no one figured me out ot be human…. yet."

    mc "So far so good… Just have to last four more days as [mc] the Witch."

    mc "Maybe I should practice more tricks before school tomorrow..."

    jump classroom_day_two



# DAY 2 SCENES
label classroom_day_two:

    scene classroom 

    "It was hard waking up this morning, but I made it in time."

    show wendigo left
    show sk right 

    sk "I'm telling you! It would look amazing, and probably taste good."

    wendigo "First of all, I am not taking palate recommendations from someone who has a balloon for a stomach"

    wendigo "Second, no matter what you say, I will attempt to use beef bone broth to make a desert"

    wendigo "Third, I seriously doubt any of my followers would be interested in seeing anything you make"

    show sk sad at right

    sk "Ok dude, you didn't have to be such an asshole about it"

    show wendigo angry at left

    wendigo "Well I do, because everyone here treats my revolutionary social media like a joke!"

    hide sk

    show banshee at right 

    banshee "You don't have to act like you're better than everyone though!"

    hide banshee 

    show zombie 

    zombie "Yeah, you could have been a bit nicer... "

    wendigo "You know what, I am never going to sell any shoutouts to you all again!"

    zombie "I don't think anyone bought those anyway..."

    wendigo "Well actually, I was able to finance all of my trip to our local brewery through all of the money I made!"

    hide zombie 

    show sk 

    sk "Hey, my mom financed the trip for us to go to that"

    hide sk

    hide wendigo 

    show teacher

    teacher "Alright class, that's enough! You can talk about your Tweeters and your maskbooks another time."

    "Everyone goes back to their seats, with Todd still looking pissed off."

    snake "That was a ssssssick burn though"

    teacher "Hey! If you keep this up, then I'm not going to take a mice bath like I promised."

    "The snakes immediately stop making any sounds"

    teacher "Anyways, I have some announcements this morning."

    teacher "Our school werewolf Larry got a bit hungry last night, so lunch will be only vegetables today"

    "Todd face finally lightens up"

    teacher "Also, please remember to bring your permission slips for Halloween. I'm sure you're all excited to finally show off your human hunting skills, but no slip means no trip!"

    teacher "That's all for now, students."

    teacher "Please see yourselves to where you want to spend your day,  and work hard!"

    scene school_map

    "It seems like where I chose to go will be pretty important, so I should be sure in my choice before I go"
    menu:
        "Where do I go?"
        "To the gym":
            jump gym_day_two
        "To the hallways":
            jump behind_stairs_day_two

label gym_day_two:
    scene gym
    show sk at right
    show mc at left
    "I walk into the gym. Cal Um is sitting on a bench drinking some greenish grey goop."
    sk "Hey [main], how's it hanging."
    mc "Hey Cal. What's that your drinking?"
    sk "My patented \" Bone Brew \". It's chalk full of protein and vitamin K"
    "He takes a big gulp, you can hear the shake plop into his torso."
    mc "What's in it?"
    sk "Bro, get notes."
    sk "So it begins with about a cup of Whey protein. The good stuff."
    sk "Of course you need a liquid. I use 2 cups of unsweetened goat milk"
    sk "Preferably the goat was sacrificed to Baphomet"
    mc "Okay"
    sk "And then put in a whole Romanesco broccoli. Fractals are well known sources of Vitamin Pi"
    mc "Anything else"
    sk "I tend to put a half a tsp of blood of arsonists in for flavor"
    sk "But cranberry juice works well too"
    sk "Finally."
    sk "Rocks"
    mc "Rocks?"
    sk "Limestone zest, Granite oil, a pinch of sand."
    sk "Any old rocks you have lying around it your pantry."
    sk "Trust me, It's not the same without rocks"
    mc "But why rocks?"
    sk "Rocks"
    sk "..."
    sk "Anyway yeah you blend all that shit together and comes out with the one"
    sk "The only"
    sk "BONE BREW"
    menu:
        sk "So do you want a sip?"
        "Sure, pass it over":
            jump gym_day_two_sip
        "Nah, I'll pass":
                jump gym_day_two_nip

label gym_day_two_sip: 
    "Against what my gut and brain tell me, I take a light sip of the shake. It's surprisingly spicy. Maybe that's the blood, maybe the rocks? Who knows?"
    sk "So, how is it? Do you feel more solid already?"
    menu: 
        mc "I think it's"
        "Very tasty.":
            jump gym_day_two_good
        "Maybe not for me.":
            jump gym_day_two_good
        "Ugh, how do even you swallow this?":
            jump gym_day_two_bad

label gym_day_two_nip: 
    mc "I'm already stuffed from breakfast, and I don't think I'm going to do any exercises today."
    mc "Such a thick shake like that would have me bursting."
    sk "Bursting?"
    mc "It's a figure of speech, just meaning I would be full."
    sk "Full?"
    mc "Where does all the stuff that goes through your mouth go?"
    sk "None of your business [main]."
    mc "Okay cool"
    $ skeleton_sus += 5
    jump classroom_day_three
    
label gym_day_two_good:
    sk "Gotcha"
    sk "Cool cool"
    mc "I can really taste the fractals in it."
    sk "RIGHT? It's the best part"
    mc "Maybe instead of arsonist you should try something purer?"
    sk "What are you thinking?"
    mc "I was down at Hades-Mart and saw some composer blood."
    sk "Bach blood? HELL YEAH."
    jump classroom_day_three

label gym_day_two_bad:
    sk "You? You don't like it"
    mc "God no, I can feel fucking rocks scraping my throat"
    sk "But, but it's my old man's recipe."
    sk "He made it after my uncle died of scoliosis"
    mc "Skeletons can get scoliosis?"
    sk "If are bones are too weak the spine curves and one day it shatters."
    sk "I saw my uncle crack under his own skull."
    sk "I promised myself I would not let that happen to anyone else."
    sk "Including my friends"
    sk "But if you really don't like it, that's fine"
    sk "I guess"
    jump classroom_day_three




    #The scenes for day three
label classroom_day_three:

    scene classroom

    show main character at left

    show skeleton at right

    sk"Hey! I was just waiting for you to come in!"

    "Oh no"

    sk"Why was Saturday stronger than Wednesday?"

    "I don't think I want to know the answer"

    sk "Because Wednesday is a WEEKDAY"

    sk "Do you get it?"

    sk "It's because week and weak are pronounced the same!"

    show banshee at left

    banshee "That was pretty lame"

    sk"Ha! Do you think you got something better?"

    banshee "Of course I do, but I doubt you would get it"

    sk "Try me"

    banshee "Well, its actually about a friend of mine..."

    banshee "So, she walks into a heavy metal bar"

    "They take a brief pause"

    banshee "And she said 'Ow, that hurt"

    "The jokes are getting worse"

    hide sk

    show zombie at right 

    zombie "Both of you are really immature."

    banshee "What? Having some good laughs makes me feel alive, which might be why you don't like them"

    zombie"Hey! I can have a good laugh, just not at stupidity like you."

    banshee "Yeah, well prove it!"

    zombie "I don't have to prove anything to you"

    banshee "I knew you were all talk"

    zombie "Fine! What is a simile then?"

    banshee "Isn't that when people are smiling or some shit"

    zombie "No! It's like a metaphor"

    banshee "I don't understand"

    zombie "It was a joke"

    banshee "About what?"

    zombie "The relation between similes and metaphors"

    banshee "I don't get it."

    zombie "You wouldn't"

    hide banshee

    show wendigo at left

    wendigo "That was actually pretty good, but don't expect anyone else to get it"

    zombie "Thanks, at least someone understands it."

    wendigo "Of course I do! However, I know one only the finest of intelligent people would understand"

    zombie "Yeah, I'm sure of it..."

    wendigo"Truly, only those with the highest IQ could even hope to understand the complexity of my joke enough to make it laughable for them"

    wendigo "Have any of your heard about this band called 1023MB, they haven't had any gigs yet!"

    hide zombie

    show sk

    sk "Dude, even I got that."

    sk "I don't know if you've been exclusively telling jokes to your parents, but anyone from this century would get that"

    wendigo "That's not true"

    hide sk

    hide wendigo

    show teacher at middle 

    teacher "It's true that every single one of my snakes sighed at that joke, so I would say it hits with most people"

    teacher "Since we're all in a joking mood today, I suppose I can share you with one of my greatest treasured jokes"

    teacher "What would you call taking a selfie with a cobra?"

    snakes "A missssss-take!"

    teacher "Finally! We've rehearsed that line so many times!"

    "The snakes are headbutting each other, but it seems to be celebratory"

    teacher "Well, that put them in a positive mood, which, as you know, also makes me pretty happy"

    teacher "But, we have run out of homeroom time, so you should all get going! See you all tomorrow!"

    scene school_map

    menu:
        "Where do I go?"
        "To the gym":
            jump gym_day_three
        "To the hallways":
            jump behind_stairs_day_three

label gym_day_three:
    "One of the walls of the gym is scorched. Quite the game of dodgeball. Cal is lifting weights in the back"
    sk "HEY BRO are you ready for the Halloween banger on friday?"
    mc "Yeah, I've been prepping all week for it."
    sk "Hell yeah man"
    mc "It's pretty exciting"
    sk "Do you think chicks will be there?"
    mc "I assume so"
    sk "Fuck yeah bro, fuck yeah"
    mc "You like parties don't you"
    sk "Bromeat, parties are my life"
    mc "I haven't really been to one"
    sk "You are missing the hell out."
    mc "What do you tend to do at a party?"
    sk "Well first I down like 5 fermented bone brews. That's my pre-pre-pre-game."
    mc "Damn, you must be hammered once the party comes."
    sk "Nah, alcohol doesn't really work on me. Don't tell the football team that, they think I'm a king with how much shit I can down"
    mc "So how do you inebriate yourself?" 
    sk "Well my brain is like, in a different dimension."
    mc "Yeah, sure"
    sk "So I just move tessacterly like 5 paces and walk back. That get's me pretty boned"
    mc "I can't say I understand how that works, like at all."
    sk "Well, it's technically against the rules to interdimensionally travel at school."
    sk "But no one's looking"
    sk "I'll just take one step"
    hide sk
    mc "Woah, where did he go?"
    show sk at right
    sk "HEEEEEEEYYYYYYYYYY bro. Fuck I hit a wall and that jostled me aro…"
    sk "Woah look at that cat! Can-ca-can I pet?"
    mc "Yeah sure"
    sk "Hey kitty kitty. Hey man, I'm gonna be straight wit you. That's a cute cat."
    sk "Shhhhhhiiiiittttt"
    sk "HAHHAHAHAHAHAHAHAHA"
    sk "Did you know i've never seen a cat before?"
    sk "I can't belive how soft it is"
    sk "WOOOOOAHHHH my jaw is tinglyingngihgngng."
    sk "ngngnngnngngngngngnzzngnzgnzznnzzzzzz"
    sk "zzzzzzzzzzz"
    "He falls asleep for a moment"
    sk "Hey, like, I'm not drunk or anything?"
    menu:
        "What should I tell him"
        "You are pretty hammered":
            jump gym_day_three_help
        "Nah man, you good":
            jump gym_day_three_ignore
        "I didn't see anything, try it again.":
            jump_gym_day_three_death
label gym_day_three_help:
    sk "Wait shit? Really?"
    mc "Yeah. Maybe you should go to the nurses"
    sk "No, they would tell my parents"
    sk "Man, my dad would be piiiiyiyiyiyssssscccceeeeeedddd"
    sk "Pycid"
    sk "Pissed"
    sk "I would be grounded *burp"
    mc "Okay, um. Here, lie down on your side."
    sk "It's uncomforablebele"
    mc "Wait can you throw up?"
    sk "Not really no"
    mc "Okay, get on your back"
    mc "I'll keep watch for the rest of the period. You just relax."
    jump classroom_day_four

label gym_day_three_ignore:
    sk "Tight"
    sk "I'll get back to my weights"
    mc "Okay, you do that"
    sk "These one's"
    mc "Yeah the ones you were just using"
    "He goes to pick up the weights but trips. He falls on his head."
    sk "I'm alllllllrrriiighht. I'm allllllllrrriiigggghhhtttt"
    jump classroom_day_four

label gym_day_three_again:
    sk "Oh, can't have that dude"
    sk "Can witches move through dimensions?"
    mc "Not really no"
    sk "Okay, I'll go slow this time."
    sk "Jeronimo!"
    hide sk
    "He disappears again. Must be traveling"
    "It's taking a really long time"
    "Minutes pass"
    show sk at right
    sk "Hegugy vmnbba"
    sk "O difooofffffff feeeelllekfefe giiooigioedddoighdd"
    sk "FFDFFDDFFUYYUUUUUUUFDCCKCCCCCKCKCKKCKCKC"
    sk "*thud"
    "He falls asleep on his side. No sign of waking up."
    mc "Uh, well, thanks for the demo"
    "I shuffle out of the gym"
    jump classroom_day_four:


label end_game:
    # This ends the game.
    return

