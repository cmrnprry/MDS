# The script of the game goes in this file.

# The game starts here.

label start:

    #Characters
    #Character Main Locations
    # Banshee - Club Room
    # Zombie - Stairs
    # Skeleton - Gym
    # Wendigo - Bleachers
    define banshee = Character(_("AH"), color = "#1ff4ff")
    define zombie = Character(_("Zoë"), color ="#2ec414")
    define sk = Character(_("Cal"), color ="#bf9393")
    define wendigo = Character(_("Todd"), color ="#e6152a")
    define teacher = Character(_("Teacher"), color ="#ae15e6")
    define mc = Character(_("[main]"), color ="#424242")
    define snake = Character(_("Snakes"),color="#0d824d")

    #suspicion meter
    $ banshee_sus = 50
    $ zombie_sus = 50
    $ skeleton_sus = 50
    $ wendigo_sus = 50


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

    scene classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc
    # These display lines of dialogue.
    mc "First day at monster school!"
    mc "Yeah, monster school. Hopefully I don’t die."
    mc "This witch costume is just barely convincing enough, and if I get caught being a human, it could mean the end of me."
    jump classroom_day_one

########################################
#                                      # 
#             SCENES DAY 1             #
#                                      #
########################################
label classroom_day_one:

    show mc at left

    mc "So far, I've gone relatively unnoticed. I'm only here because I met some cool people from this school last year, and I can't go back to my assigned high school"

    mc "I spent the last year training to become a master at magicry, since after I was admitted here, I found out that you needed to be a 'monster' to attend"

    mc "I figured my best bet was to become a witch! I immediately bought the Criss Angel MINDFREAK Professional Magic Kit, and that has been the source of my tricks."

    mc "I tried to upgrade to the Penn and Teller kit, but I couldn't get it from Amazon in time"

    hide mc

    show teacher at center

    snake "Sssssso classsss"

    teacher "Excuse me! Do not address my students, that is my job."

    "The teacher slaps a snake that was going towards her neck away"

    teacher "Anyways, we have a new student here today, a Witch named [mc]"

    mc "I can hear some people start questioning what type of magic I can do"

    mc "This is what I have been training for"

    teacher "Quiet down! Be nice to our new student! They came a long way to get here"

    teacher "But I might agree with the class, I would love to see a trick"

    hide Teacher

    show mc at left

    mc "Oh boy!"

    menu:
        "What trick should I show off?"
        "Pull a quarter out of a zombie's ear":
            jump perform_quarter
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
    hide mc
    
    show teacher at center

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

    show sk at center

    sk "Hey dude! The name's Cal."

    "He tries to put his hand out to shake mine, but he is too far away and tries to act like it never happened by stroking his hair back, even though he has none. "

    "The class does not know to go in order horizontally or vertically and it is cause major social awkwardness for everyone"

    "Someone, please go."

    hide sk at center

    show wendigo at center

    wendigo "Hi, I'm Todd Howard, but you might know me from my instagram ImWendigoingVegan."

    "I do not, but I'm slightly terrified to tell him that"

    hide wendigo at center

    show banshee at center

    banshee "HI!"

    "Some cover their ears, and the teacher motions to lower their voice"

    banshee "Sorry, I forgot how loud I can be, but my name is AAAAAAAHHHHHH"

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
    ###########
    #MAP MENU 1
    ############
        "Where do I go?"
        "To the gym":
            jump gym_day_one
        "To the hallways":
            jump behind_stairs_day_one
        "To the blachers":
            jump behind_bleachers_day_one
        "To the bandroom":
            jump clubroom_day_one

                            ################
                            #Skeleton Day 1#
                            ################
label gym_day_one:
    scene gym
    show mc at left
    "I walk into the school's large gym. There's also a small gym but that's just a cardboard box where mandrakes and others play their own sports. The large gym has some equipment for everyone. I see a rather beefy…"

    "No wait, that doesn't make sense"

    show sk at right
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
    show sk happy
    sk "WOAH BRO, that shit's tight. Could you show me one?"
    mc "Yeah, sure. You want to see a spell?"
    sk "YUS, I LOVE MAGIC."
    sk "There was this motivational speaker from London or some shit, he had like a wand and made books float. Coolest day ever."
    sk "So what are you gonna do"
    mc "Uh, I have these {i}Rings of{/i}..."
    mc "{i}Rings of Cincinnati{/i}"
    show sk suspicious
    show mc suprised
    "Cincinnati? Really [main]? I thought I didn't want to die."
    "I wonder what cruel, grotesque, soul crushing, way this skeleton could make me no more."
    "Oh no he's looking mad"
    sk "{i}Cincinnati{/i}?"
    show sk
    sk "Sounds like an old guru. Cincinnati. Even saying it makes me feel more magical."
    show sk happy
    sk "Awesome bro"
    show mc happy
    mc "Ha, yeah, he's quite the famous warlock"
    "As I reach into my pocket to pull out the rings I really hope the next class isn't geography"
    show sk suspicious
    show mc
    mc "Here they are {i}the Rings of Cincinnati{/i}. Behold, two interlocking rings."
    mc "However, when I say the magic words." 
    mc "{i}Toledo{/i}."
    mc "The rings merge through each other and separate." 
    show sk happy
    sk "WOAH, how the fucking fuck?"
    mc "Magic my man"
    mc "And with the incantation:"
    mc "{i}Cleveland{/i}."
    mc "The rings re-connect. As if they were never apart."
    sk "Woah woah. Damn you really are a witch"
    show banshee
    show sk
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
    show sk angry
    sk "HNNNG"
    "The skeleton pulls with so much might, yet the plastic rings don't even bend."
    show sk
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
    $skeleton_sus += 10
    jump end_day_one

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
    $skeleton_sus += 2
    jump end_day_one

label gym_day_one_bad:
    sk "To get fit"
    mc "But you exercise muscles, not bones."
    sk "Man, what the fuck?"
    sk "What do you think instead of putting in the work I should, I don't know, take a milk bath?"
    mc "Yeah, maybe"
    sk "I know your a witch."
    sk "But to me all you are is a bitch."
    sk "I don't want to see anymore of your bitch magic"
    $skeleton_sus -= 20
    jump end_day_one      


                                ##############
                                #Zombie Day 1#
                                ##############
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

    show zombie suspicious at right

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

    show zombie angry at right

    zombie "Why did you touch me?"

    mc "I- It's part of the spectacle!"

    show zombie suspicious at right
    
    zombie "Spectacle?"

    mc "Yes! Spectacle! The best part of being a Witch is making a show of the magic."

    zombie "Riiiiggghhhttt."
    
    mc "Zombies don't make a show of, uh, eating… people..?"

    show zombie angry at right
    
    zombie "No, we don't. We just kill and eat humans and are done with it. There's nothing \"showy\" about it"

    zombie "It is fun to chase and terrify humans but we don't make a show of it. It's just what we do."

    "She gathered her things and walked away in a huff."

    mc "Well that didn't go very well…"

    $ zombie_sus -= 10
    jump end_day_one

                                #################
                                # WENDIGO DAY 1 #
                                #################
label behind_bleachers_day_one:

    scene bleachers
    show wendigo at right
    wendigo "The lighting is just right to take a picture of my stuffed banana bread french toast! "

    show mc

    wendigo "You're the new monster, right?"

    wendigo "I need some opinions, do you think that this picture would look better with some 24k golden sprinkles, or that it's fine as is"

    menu:
        "You should add the sprinkles":
            jump blechers_sprinkles
        "You should leave it as is":
            jump blechers_alone
        "It looks terrible either way":
            jump blecher_terrible

label blecher_terrible:
    show wendigo angry at right 

    wendigo"How dare you? I spent all night making fresh bread to make this look perfect for all of my followers"

    wendigo "I doubt you even know the first thing about what could make a good meal!"

    wendigo "Do you even know the difference between a souffle and a frittata?"

    wendigo "I bet you're just jealous that you aren't considered an instagram influencer!"

    wendigo "I would really appreciate it if you left me alone to my pictures!"

    hide wendigo

    mc"Well, that was kind of an asshole thing to do"

    mc "But they too are an asshole, so I don't feel too bad"

    $wendigo_sus -= 10

    jump end_day_one

label blechers_sprinkles: 
    wendigo"I totally agree! The perfection is already there, now we just need the cherry on top"
    wendigo "Well, it actually already has a cherry on top, these are just the 24k real gold on top!"
    $ skeleton_sus += 10
    jump bleacher_filter

label blecher_alone:

    wendigo "While it's kind that you consider this pure beauty, you must also have an eye to see where it can improve, and where it can improve is the toppings"

    wendigo "I wouldn't expect you to know, seeing as though you seem to not have been exposed to the wonders of social media yet, but if you stay around me, you would learn"

    $wendigo_sus += 5

    jump bleacher_filter

label bleacher_filter:

    wendigo "Here, would you like to take the picture while I hold the lighting to perfectly reflect the light to the camera"

    "I help him take the picture"

    menu:
        "Do you use a filter?":
            jump bleacher_teach_filter
        "It looks great!":
            jump bleacher_end

label bleacher_teach_filter:
    
    wendigo "What's a filter?"

    mc "It's a way to edit pictures on instagram?"

    wendigo "WHAT?"

    mc "Yeah, they've been around since the beginning!"

    wendigo "Woah! Could you show me!"

    mc "Of course."

    "I spend a good chunk of my day showing Todd how to properly use instagram, and I had a surprisingly good time"

    $wendigo_sus += 10

    jump end_day_one

label bleacher_end:
    wendigo"I do also deem it ready for posting!"

    wendigo"Thank you for your help, you would make a good assistant photographer for my account"

    wendigo "But that's a conversation for another day."

    wendigo "I should be heading out now, but we could talk again tomorrow. I spend most of my time around here."

    $wendigo_sus +=5

    jump end_day_one

                            #################
                            # BANSHEE DAY 1 #
                            #################
label clubroom_day_one:
    scene clubroom
    show mc at left

    "I don’t feel like going to my next class so I wander the halls for a few minutes, trying to find a place to relax. This really is a school for monsters. I’ve held it together so far."

    "I find a dark room with a slightly ajar door and slip inside. Even with the lights off  Ican see the faint outline of a drum set and some guitars on stands. This must be-"

    "The light flips on."

    show banshee at right
    banshee "Oh hi!!"

    "I jump involuntarily and turn around."

    banshee "Sorry. I know I can be loud. Are you here to join band?"
    mc "This is the band room?"
    "I have never seen a school band room that looked this cool."
    banshee "Yeah and the cheerleading squad!! I fucking love this school!" 
    mc "That's really cool! What do you play?"
    banshee "I'm the lead guitarist and vocalist for Bandshee!"
    menu:
        "You wanna hear a song?"
        "Yeah":
            jump club_day_one_silence
        "I'm good thanks.":
            jump club_day_one_song

label club_day_one_song:
    "Banshee picks up a red electric guitar and sits on top of a desk covered in pen marks."
    banshee "This one is called \'One Day.\'"
    "Banshee unleashes a deluge of guitar chords and screams. They seem to be saying words, but I can't make out any of them in the barrage of discordant sound." 
    "Still, they look so happy when they're playing that I start to feel it too."
    "When Banshee stops playing, they set the guitar down and stand beside me."
    banshee "Did you like the song?"
    menu:
        "The song was "
        "super cool!!":
            jump club_day_one_goodsong
        "not good...":
            jump club_day_one_badsong

label club_day_one_goodsong:

    mc "It was super cool."
    show banshee happy
    banshee "Really? That makes me so happy! I'd love for you to hear the whole band play!"
    show mc happy
    mc "Me too."
    jump club_day_one_good

label club_day_one_badsong:
    #sad banshee
    banshee "Oh. Okay."
    mc "Sorry dude. I gotta be honest."
    banshee "No hard feelings. Really."
    jump club_day_one_bad

label club_day_one_silence:
    banshee "Okay! We'll be playing at the next pep rally so you'll probably hear us then."
    "An awkward silence ensues."
    banshee "You're a witch right?"
    mc "Yeah why?"
    banshee "I love magic! Show me some!"
    "The moment of truth. Kind of..."
    mc "Alright!"
    menu:
        "Make a scarf appear out of thin air.":
            jump club_day_one_appear
        "Make a card levitate.":
            jump club_day_one_levitate

label club_day_one_levitate:
    "I pull out a playing card and make it float between my hands!"
    banshee "That's pretty cool."
    mc "I try."
    $ banshee_sus -=10
    jump club_day_one_good
    label club_day_one_appear:
    "I steel myself then start my trick."
    mc "Watch this."
    "I pull a thin silk scarf from my sleeve with a flourish."
    mc "Tada!"
    banshee "That was...Okay."
    #banshee suspicious
    $ banshee_sus +=10
    jump club_day_one_bad

label club_day_one_bad:
    "Banshee leaves without a word. The light turns off."
    mc "I think I may have done something wrong."
    jump classroom_day_two

label club_day_one_good:
    banshee "I usually hang out here around this time if you wanna hear me play or just talk."
    mc "Sounds good! I'm usually just around."
    banshee "I'll see you around then."
    "Banshee smiles at me before heading out."
    jump classroom_day_two

###############
#END OF DAY ONE
###############
label end_day_one:
    scene black
    $ day += 1

    mc "Well today was interesting…"

    mc "I thought my first day at Creature Academy would go a lot different, but everyone seems very nice."
        
    mc "And no one figured me out ot be human…. yet."

    mc "So far so good… Just have to last four more days as [mc] the Witch."

    mc "Maybe I should practice more tricks before school tomorrow..."

    jump classroom_day_two

########################################
#                                      # 
#             SCENES DAY 2             #
#                                      #
########################################
label classroom_day_two:

    scene classroom 

    "It was hard waking up this morning, but I made it in time."

    show wendigo at left
    show sk at right 

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
   
   ##### MENU MAP ## ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
    menu:
        "Where do I go?"
        "To the gym":
            jump gym_day_two
        "To the hallways":
            jump behind_stairs_day_two
        "To the bleachers":
            jump behind_bleachers_day_two
        "To the bandroom":
            jump clubroom_day_two

                        ###################
                        # SKELETON DAY 2  #
                        ###################
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
    jump end_day_two
    
label gym_day_two_good:
    sk "Gotcha"
    sk "Cool cool"
    mc "I can really taste the fractals in it."
    sk "RIGHT? It's the best part"
    mc "Maybe instead of arsonist you should try something purer?"
    sk "What are you thinking?"
    mc "I was down at Hades-Mart and saw some composer blood."
    sk "Bach blood? HELL YEAH."
    $ skeleton_sus += 10
    jump end_day_two

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
    $ skeleton_sus -= 10
    jump end_day_two

                            ###############
                            #WENDIGO DAY 2#
                            ###############
label behind_bleachers_day_two:
    scene bleacher
    
    show wendigo at right
    "As I approach the bleachers, I can see Todd preparing some type of food"
    wendigo"Ok, so you're supposed to now combine the chicken with the kale, but I brought my tofu substitute, which will make this recipe even better!"
    show mc at left
    wendigo "Oh, hi"
    wendigo "I typically come out here to prepare my meals and eat, because some people don't appreciate what I make"
    wendigo "All of the heathens that go to this school think meat is the epitome of delectable meals."
    wendigo "I swear, you could literally serve them a unskinned deer and they would fight over who gets the first bite"
    wendigo "What do you think about their eating habits? Do you actually value flavor and meaning, or you just want what you can get?"
    menu:
        "How do I feel about food?"
        "You should always aim to make the best food you can":
            jump bleacher_good_food
        "Meat Good":
            jump bleacher_bad_food

label bleacher_good_food:
    wendigo"Definitely, I was fairly confident you were not like the others, and this confirms it."
    wendigo "I personally stray away from meats, and find substitutes any time I can"
    wendigo "The flavors never combine well, and there's no definite way for me to know the meat was obtained ethically"
    wendigo "I've thought about cutting gluten out of my diet, but I simply can't go without my Trader Joe's chocolate dunkers."
    wendigo "There's a whole world of culinary expertise that I can't wait to spend my life exploring!"
    wendigo "Now, are you as excited about food as I am, or do you just moderately enjoy it?"
    menu:
        "How much do I enjoy food?"
        "It is the only thing that gives me happiness":
            jump bleacher_happy_food
        "I do not know too much about the food world":
            jump bleacher_sad_food

label bleacher_bad_food:
    wendigo "I must admit, I'm a bit surprised"
    wendigo "I pegged you as different from everyone else, but you have proved your incompetence"
    wendigo "You should probably go, I don't want to keep you bored with my culinary expertise."
    "I think this guy takes his food way too seriously..."
    hide mc
    $wendigo_sus -=10
    jump end_day_two

label bleacher_happy_food:
    wendigo "Wonderful, I see you are a monster of culture"
    wendigo "You can truly learn a lot about a person based on what they eat"
    wendigo "I hope that when people see my meals, they understand that I'm a worldly being, with a deep understanding of what it means to live a full life"
    wendigo "And, based on what you just told me, I peg you very similarly"
    "Wow, I have not hear Todd say such a nice thing!"
    "I really hope we can further our friendship!"
    $wendigo_sus += 10
    jump end_day_two

label bleacher_sad_food:
    wendigo "That's acceptable, as I'm sure that if you keep hanging with me, I can expose you to the world"
    wendigo "There's so much to discover, and I would love to help someone see into it."
    wendigo "If you're willing to, that is"
    wendigo "And, of course, I don't expect you to make such an important decision now"
    wendigo "But consider it. It would be cool to have a Food Friend"
    "Wow! That's definitely an interesting offer"
    $wendigo_sus +=5
    jump end_day_two


                                ###############
                                #BANSHEE DAY 2#
                                ###############
label clubroom_day_two:
    scene clubroom
    show mc at left
    show banshee at right
    banshee "Hey [mc]! Great to see you!"
    mc "Hi Banshee!"
    "Banshee it sitting on the blue rug, strumming absently at their guitar. When they are playing with 9000% aggression, they actually sound good??"
    "I sit beside them and pull out a notebook to doodle in, nodding along to the beat of Banshee's guitar."
    mc "You play really well!"
    banshee "Thanks!! I'm just playing around though."
    "Their voice contrasts starkly with the gently strumming. I don't start this time. I'm getting used to it."
    mc "How do you do it all?"
    banshee "Hmm?"
    mc "You compose original songs, play lead in the school's band."
    mc "You're a cheerleader too right?"
    banshee "Yeah!"
    banshee "I just like making other people happy. That's how I get my energy."
    banshee "What do you like to do?"
    "After spending all my spare moments on practicing magic to blend in here, I'm not sure I do anything just for fun anymore. "
    mc "I- "
    menu:
        "Do magic tricks":
            jump club_day_two_truth
        "Play ukelele":
            jump club_day_two_lie_music
        "Play soccer":
            jump club_day_two_lie_sports
    
label club_day_two_lie_sports:
    banshee "Oh what position do you play? I love soccer!"
    "Shit" 
    mc "I'm a starter." 
    "Starter. That is a soccer term, right?" 
    mc"I don't know much and I'm not very good."
    banshee "You’ll get better I believe in you!!"
    "Banshee seems a little uneasy, but is sweet as always."
    $ banshee_sus -= 5
    jump end_day_two

label club_day_two_truth:
    mc "Actually I do magic tricks,"
    banshee "isn;t that just using your magic?"
    mc "Nope. There are humans with no magic powers who pretend they have them. It's pretty amazing to look at them."
    banshee "Sounds awesome! Can I see one?"
    "Fuck. I should have known this would happen. If they see that the tricks look the same as my actual magic, I'm screwed."
    menu:
        "Do one anyway.":
            jump club_day_two_trick
        "Change the subject":
            jump club_day_two_cheer

label club_day_two_trick:
    mc "What's that behind your ear?"
    banshee "There's nothing behind-"
    "I deftly put my hand behind their ear and pull a quarter out from between my fingers."
    banshee "Wow!! That's so cool!"
    "Good thing Banshee is so positive and easily impressed."
    mc "Human tricks are all about misdirection and illusions! The quarter was actually in my hand the whole time!"
    $ banshee_sus += 10
    jump end_day_two

label club_day_two_cheer:
    mc "You need this specific kit to do them and I left it at home."
    banshee "Oh too bad."
    mc "Sure is. Anyway, do you have a favorite cheer."
    banslee "omigod yes. Wait Ill show you jist let me-"
    "They jump up and set the guitar on a stand."
    banshee "Hunters win the fight. Hunters make it right, Try to keep us from that three, we’ll attack your family.!! Go Hunters!"
    "Banshee performs the simple arm and leg movements with the grace of a dancer and end the cheer with a perfect split. I'm in awe."
    "I start to clap without thinking"
    banshee "OMG stop!! You're gonna make me blush,"
    show banshee blushie
    "I don't mind seeing Banshee like this. I want to make them blush again "
    $ banshee_sus +=10
    jump end_day_two

label club_day_two_lie_music:
    mc "I write songs."
    banshee "We have that in common. Can I hear one of your songs?"
    "I did not think this far ahead."
    mc "Um… they're kinda personal, so I keep them to myself."
    banshee "Oh, I see. Maybe you'll share one with me sometime."
    "I shrug."
    mc "Maybe."
    $ banshee_sus -=5
    jump end_day_two


                                ##############
                                #ZOMBIE DAY 2#
                                ##############
label behind_stairs_day_two:
    
    scene hallway

    "Zoë was once again hiding herself behind the stairs with her nose buried in a book. I sat next to her."

    show mc at left

    show zombie at right

    mc "Hey Zoë, whatcha reading?"
    
    zombie "I'm reading about brains in hopes to figure out what makes a brain smart and how to best find these smarter brains."

    mc "Uhh.. Smart… Brains?"

    "She sighed and closed her book."

    zombie "I doubt you would understand, but when a Zombie eats a human brain, we can absorb the knowledge of that person. So I am reading about how to find people like that."

    mc "That's pretty... cool?"

    show zombie blushie at right

    zombie "Really? Most people think my obsession is a little… odd even for a zombie."

    menu:
        "Knowledge is power, so you'll have the last laugh.":
            jump zday_two_choice
        "It is a little strange.":
            jump zday_two_choice2
        "As long as you don't touch my brain, I don't care what you read about.":
            jump zday_two_choice3

label zday_two_choice:
    
    show zombie happy at right
    
    zombie "That's what I said! Just you wait!"

    mc "So what is the book on exactly? Surely there can't be a book about how to find smart brains."

    zombie "Nope! \"Smart Brains and Where to Find Them!\" I found it at the school library!"

    "Zoë held up a book where the front cover showed a zombie munching on a brain."

    "I winced slightly."

    show zombie at right

    zombie "It's very informative. I learned all the best ways to find more intelligent brains! Apparently, it's very common to find then in places you'd least expect it. Since the humans with these brains are smarter than normal humans, sometimes they hide {i} among {/i} us so we don't think to suspect them."

    "Zoë's eyes were wide as she talked and flipped through her book. I started sweating."

    mc "Th-that can't be right. No human can be that smart. Ha…"

    zombie "The book also mentioned that. It says the next best place to look is on social media. Apparently, smart humans feel the need to flex on people and prove their intelligence all the time."

    mc "That's definitely your best bet."

    zombie "You think so?"

    mc "Oh yeah. Definitely. There's no way a human would ever pose as a monster. That's a lot of risk on their part. Like what if they get caught?" 

    zombie "That's very true. The human I'm looking for would never want to risk their own death."

    mc "Well, if you ever need help finding one of these humans let me know."

    zombie "How would you be able to help?"

    mc "With the help of this tiny black box, I can channel the power of lightning!"

    "I pulled out a small taser."

    mc "And with this power, I can incapacitate any human I come across."

    show zombie_blush at right

    zombie "You would use your magic to help me?"

    mc "Of course! We're friends right?"

    "And if I help you, then you're less likely to try and eat me."

    zombie "Friends, yes!"

    "Zoë and I spent the rest of the school day discussing the best ways to find and capture the one human she's looking for."

    $ zombie_sus += 10

    jump end_day_two

label zday_two_choice2:

    show zombie angry at right

    zombie "I don't know why I even bother."
    "She shoved her book in her bag."

    mc "I'm sorry. I didn't mean-"

    zombie "Save it. I don't need to hear anything more from {i} you {/i}."

    "She started reading her book and didn't respond to any of my apologies. After a few moments I left to got to my next class."

    jump end_day_two

label zday_two_choice3:
    
    show zombie_sus at right

    zombie "And why would I? You're a Witch?"

    mc "Ah yes, of course! That was a joke!"

    "I started laughing hoping she would join along, but she just stared at me, confused."

    mc "A very bad joke. I think I'll just stick to magic."

    zombie "You're not even very good at that…"

    mc "I'll show you! Just watch as I disappear!"
    
    "I pulled one of the smoke bombs out of my pocket and threw it on the ground."

    zombie "What the f-"

    "I quickly ran up the stairs and to my next class while she was distracted."

    $ zombie_sus -= 10

    jump end_day_two

##### END DAY 2 #####
label end_day_two:
    mc "Day two at Creature Academy over and done. Only a couple days left."
    
    mc "I didn't know that monster used Instagram?"

    mc "I figured they had their own brand like… Insta-Ghoul or something."

    mc "Or maybe that's like calling it Insta-Human?"

    mc "And why wouldn't they just use normal Instagram? It all the same, right?"

    "I pull out my phone and scroll through the monster side of Instagram."

    mc "It turns out I was very wrong and the monster side involves a hell of a lot more blood and gore."

    mc "I really hope I can survive til the end of the week. I would really hate to become one another post on someone's account…"

    jump classroom_day_three




########################################
#                                      # 
#             SCENES DAY 3             #
#                                      #
########################################


label classroom_day_three:

    scene classroom

    show mc at left

    show sk at right

    sk"Hey! I was just waiting for you to come in!"

    "Oh no"

    sk"Why was Saturday stronger than Wednesday?"

    "I don't think I want to know the answer"

    sk "Because Wednesday is a WEEKDAY"

    sk "Do you get it?"

    sk "It's because week and weak are pronounced the same!"

    hide mc at left

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

    show teacher at center 

    teacher "It's true that every single one of my snakes sighed at that joke, so I would say it hits with most people"

    teacher "Since we're all in a joking mood today, I suppose I can share you with one of my greatest treasured jokes"

    teacher "What would you call taking a selfie with a cobra?"

    snake "A missssss-take!"

    teacher "Finally! We've rehearsed that line so many times!"

    "The snakes are headbutting each other, but it seems to be celebratory"

    teacher "Well, that put them in a positive mood, which, as you know, also makes me pretty happy"

    teacher "But, we have run out of homeroom time, so you should all get going! See you all tomorrow!"

    scene school_map
##### MENU MAP ## ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
    menu:
        "Where do I go?"
        "To the gym":
            jump gym_day_three
        "To the hallways":
            #NOT IN
            jump behind_stairs_day_three
        "To the bleachers":
            #NOT IN
            jump behind_bleachers_day_three
        "To the bandroom":
            jump clubroom_day_three

                            ################
                            #SKELETON DAY 3#
                            ################
label gym_day_three:
    scene gym
    show mc at left
    "One of the walls of the gym is scorched. Quite the game of dodgeball. Cal is lifting weights in the back"
    show sk at right
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
            jump gym_day_three_death

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
    $ skeleton_sus += 10
    jump end_day_three

label gym_day_three_ignore:
    sk "Tight"
    sk "I'll get back to my weights"
    mc "Okay, you do that"
    sk "These one's"
    mc "Yeah the ones you were just using"
    "He goes to pick up the weights but trips. He falls on his head."
    sk "I'm alllllllrrriiighht. I'm allllllllrrriiigggghhhtttt"
    $ skeleton_sus -= 5
    jump end_day_three

label gym_day_three_death:
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
    $ skeleton_sus -= 15
    jump end_day_three


                                ###############
                                #WENDIGO DAY 3#
                                ###############
label behind_bleachers_day_three:
    scene bleachers
    
    show wendigo at right
    show mc at left
        
    "As you approach, you notice that Todd has something lit in his hand"
        
    wendigo "Hey, [main], what's up?"
        
    wendigo "I'm just trying to relax before I have to go back and pretend to care about being here"

    show wendigo angry 

    wendigo "You aren't going to tell anyone, right?"

    menu: 
        "Should I tell?"
        "Nah, its fine":
            jump bleachers_dont_smoke
        "Of course I won't, if you share":
            jump bleachers_smoke
        "It is my moral obligation to expose you":
            jump bleachers_expose

label bleachers_dont_smoke:
    wendigo "Thanks"
    "He takes another hit of whatever it is that he is smoking"
    wendigo "You know, I'm able to smoke this, and I probably wouldn't get in trouble"
    wendigo "But this shit is still illegal here! There's people in jail for just wanting to feel calmer!"
    wendigo "Isn't that some bullshit?!?"
    wendigo "They literally just want to arrest people they think are dangerous"
    wendigo "But they aren't! The rich just took everything from these people "
    wendigo "We truly live in a society, don't we?"
    "I feel like he's trying to make a valid point, but is too incapicated to string his words together well."
    "He takes a few moments to catch his breath, which he lost with how fast he was talking"
    wendigo "You know, I should probably get going anyways"
    wendigo "I have a reservation at a raw pizza kitchen, and I can't go reeking of weed"
    "He leave very suddenly, and you're left alone to think about how we do, in fact, live in a society."
    $ wendigo_sus+=5
    jump end_day_three

label bleachers_smoke:
    wendigo "I didn't know you were cool enough to smoke!"
    wendigo "Come on over, I got enough to share"
    "You breath in the smoke from the pipe. It fills your lungs immediately, and even though you feel a large urge to cough, you keep it in to prove your coolness"
    wendigo "Man, that was..."
    wendigo "Huge! I can't even take puffs that big! I hope you know your tolerance, because this can get you fucked up!"
    "I do not know my tolerance"
    wendigo "But man, do you know what I've been thinking about a lot recently?"
    "I think I have fully lost my ability to speak"
    wendigo "Capitalism man!"
    wendigo "It's shit!"
    wendigo "We are promised this life where the hardest workers get the best, but it's not true!"
    wendigo "All that happens is a cycle where the rich stay rich and the poor stay poor, forever blaming themselves for not having a better life."
    wendigo "And they don't even realize that they were set up to be like this"
    wendigo "Forever hoping that one day, they'll be just lucky enough to feel stable"
    wendigo "But for most of them, that day will never come!"
    "I think I heard most of what Todd just say, but I can't find any words to respond with"
    wendigo "Sorry about that rant..."
    wendigo "Hey, you're not actually looking too good"
    wendigo "The strand we had was called Hades' Lettuce, and it definitely packs a punch if you don't take it slow"
    wendigo "However, you should be good if you just rest for a bit, it wears off pretty quickly"
    "My mind can only focus on the word rest, and a nap does sound incredible right now"
    "As I drift into sleep, I hear Todd sarcastically say 'Goodnight'"
    $ wendigo_sus +=10
    jump end_day_three

label  bleachers_expose:
    wendigo "Oh yeah, everyone talks about their moral obligations, but they never actually practice them!"
    wendigo"You can go and expose me, but that isn't going to solve the bigger issues at hand"
    wendigo "You know what I'm talking about right?"
    wendigo "I'm talking about..."
    wendigo "Capitalism!"
    wendigo "It's the reason people suffer! It's the reason we are all damned to a hell worst than anything Hades could provide!"
    wendigo "You know what, I hope you tell someone about this, and I hope they arrest me"
    wendigo "Because then, and only then, and I destroy the system from the inside out"
    wendigo "So go! Leave me! Get me arrested!"
    "You leave the bleacher, not having any intention to report the extremely high hipster"
    $ wendigo_sus-=10

    jump end_day_three

                                    ###############
                                    #BANSHEE DAY 3#
                                    ###############
label clubroom_day_three:
    "Banshee isn't in the band room when I get there. I sit on the carpet to wait."
    "I close my eyes for a moment."
    banshee "[main]" 
    mc "AAH!"
    banshee "Sorry! Sorry. Hi."
    mc "Hey."
    "I want to ask Banshee something."
    menu: 
        "Are you upset about something?":
            jump club_day_three_upset
        "How's your day been?":
            jump club_day_three_okay

label day_three_upset:
    banshee "How did you know?"
    mc "You're not smiling like usual. What's wrong?"
    banshee "It's just that Halloween's coming up, and there's this big tradition of going out and hurting humans."
    "I nod to let them know I'm listening."
    banshee "And I don't actually want to hurt anyone! I can't help but think of how many people are gonna get hurt or die. How many people won't be able to add to the happiness of the world."
    menu:
        "I understand. It scares me too.":
            jump club_day_three_oops
        "I understand. I get sad too.":
            jump club_day_three_yas

label club_day_three_oops:
    banshee "I'm not scared. More sad."
    "A beat of quiet passes. A moment that lasts too long."
    banshee "Why would a witch be scared on Halloween?"
    mc "I get anxious around crowds!"
    "..."
    $ banshee_sus += 10
    jump club_day_three_end
    
label club_day_three_yas:
    banshee "Exactly!"
    $ banshee_sus -=10
    jump club_day_three_end

label club_day_three_end:
    banshee "The only reason for me to go out would be to get people to listen to my songs!"
    banshee "I only hurt people with my voice when I get enormously sorrowful-and death does that to me- so I'm gonna chill at home alone that night. Maybe write a song."
        
    menu:
        "I’d love to hear it.":
            jump club_day_three_good
        "Good luck with that!":
            jump club_day_three_bad

label club_day_three_good:
    banshee "Maybe I'll play it for you."
    "Their smile is back and bright. I'm glad."
    banshee "I'll see you [mc]!"
    show mc blushie
    "I don't know why my cheeks warm"
    $ banshee_sus -= 10
    jump end_day_three

label club_day_three_bad:
    banshee "Thanks. I'll see you."
    mc "I fiddle with my thumbs until they leave."
    jump end_day_three


                                    ##############
                                    #ZOMBIE DAY 3#
                                    ##############
label behind_stairs_day_three:
    "When I reach the Zoȅ's  hiding spot, she does not have her nose buried in a book, but instead is thoughtfully writing in what looks to be a journal."

    show zombie at right

    show mc at left

    mc "No book today Zoȅ?"

    "I sat down beside her and leaned over to look at her journal."

    mc "Whatcha writing?"

    zombie "Oh [mc], I have given up my quest. I do not think the human I'm looking for exists! So I am wallowing in my anguish by writing poetry."

    "She hands me her journal."

    zombie "Read it if you want."

    "Oh, human of mine"
    "With a brain so divine"
    "Where are you?"
    "Where do I look to?"
    "I've searched far and wide"
    "But you continue to hide"
    "Now I am dejected"
    "Yet you remain unaffected"
    "I pray for the day we find one another"
    "And then..."

    "The poem devolves into how she would kill and prepare the human before she ate their brain."

    menu:
        "This is really good!":
            jump z_day3_choice
        "Could be better.":
            jump z_day3_choice2
        "It was good until…":
            jump z_day3_choice3

label z_day3_choice:
    show zombie_happy at right

    zombie "Really?"

    mc "Yeah! It really, ah, tells you what you're feeling. Straight to the point."

    zombie "You think? I thought I was very clever with my word choice. Although it's not as profound as I would have liked."

    "She flipped through her journal and showed me another."

    zombie "Here read this!"

    "Humans humans are so great"
    "I want to take them out on dates"
    "These dates will be oh so fun"
    "I'll hit and hit until it's done"
    "They'll beg and plead but I won't care"
    "Their screams and cries make a good pair"
    "With the wine I brought"
    "Time to feast"

    "I winced. Are all monsters like this?"

    mc "This one is even better!"

    show zombie blushie at right

    zombie "I'm happy you like it. Want to read more?"

    "I nod and we spend the rest of the day reading, and even writing some new, poetry."

    $ zombie_sus += 10

    jump end_day_three

label z_day3_choice2:

    zombie "You think so…?"

    "She sadly looked at her journal."

    mc "I mean that doesn't mean there's no room for improvement. You've got a good base!"

    "She perked back up."

    show zombie happy at right

    zombie "You're right!"

    mc "And if you keep working you'll get better!"

    zombie "Yeah!"

    "For the rest of the day you encouraged Zoȅ to keep writing better and better poetry."

    $ zombie_sus += 5

    jump end_day_three

label z_day3_choice3:

    zombie "Until what?"

    mc "All the, uh, murdery parts…"

    show zombie angry at right

    zombie "Teacher said that was the best part."

    mc "Oh well what do I know hahahhaha."

    zombie "Obviously, nothing about poetry."

    show zombie suspicious at right

    zombie "And what kind of Witch are you? I thought you would like the part about using their bones for stew? Don't you do that but for potions?"

    mc "I…"

    "I panicked. How stupid could I be?"

    mc "Oh did you hear the bell? I gotta run!"

    $ zombie_sus -= 10

    jump end_day_three


####### END DAY 3 #########
label end_day_three:
    scene classroom
    mc "Tomorrow's the big day."

    mc "I don't know if I should be scared or excited. On one hand I {i} probably {/i} won't be eaten but on the other, other humans will be.."
        
    mc "I really didn't expect monsters to make bad puns the same way humans do…"

    mc "Maybe we're not so different?"

    mc "...."

    mc "No that can't be it. Humans don't kill and main other living beings for pleasure or anything like that."
        
    mc "We just hunt animals for sport."

    mc "Wait…"

    jump classroom_day_four

########################################
#                                      # 
#             SCENES DAY 4             #
#                                      #
########################################
label classroom_day_four:

    "As I approach the classroom, I can hear loud commotion coming from within"
    
    scene classroom 
    show zombie at right

    show banshee at left

    zombie "He is such a good boy!!"

    banshee "I know! Everytime I see him I absolutely gush"

    zombie "Have you ever met him? I know Hades sometimes brings him to the dog park, but I think he goes at weird hours"

    hide banshee 

    show wendigo at left

    wendigo "Who are you guys talking about?"

    zombie "Cerberus, he's Hades's dog and guards the underworld!"

    hide zombie

    show sk at right

    sk "Yoooo , do you mean the amusement park?"

    wendigo "Yeah, I think his main task is guarding the dead, but he does venture to the amusement park on Fridays!"

    sk "We should go see him this Friday! I want to pet him!"

    hide wendigo

    show zombie at left 

    zombie "I don't like amusement parks... "

    zombie "I rather see him at the dog park"

    sk "What do you mean! You don't love the exhilaration you feel when you're zooming towards the ground at 200 mph?"

    zombie "No, I don't. Other things excite me more in death."

    hide zombie 

    hide sk

    show teacher at center 

    teacher "I think there's more important reasons you can't go to the underworld on Friday"

    "The class goes silent even though the teacher is clearly waiting for an answer"

    snake "sssssince no one has ssssspoken up, the ansssswer is Halloween"

    teacher "Yes, thank you."

    teacher "I hope you have not forgotten the night this entire year has been preparing you for"

    teacher "This night will be special for all of you and you should all be excited"

    teacher "Also, we give you the day off to prepare, so tomorrow will be the last homeroom of the week. "
     
    teacher "Speaking of which, you all should go off to study now, I will see you all tomorrow!"

    scene school_map 
    menu:
    ######### MENU MAP############ # # # ##### # #  ##
        "Where do I go?"
        "To the gym":
            jump gym_day_four
        "To the hallways":
            jump behind_stairs_day_four
        "To the bleachers":
            # NOT WRITTEN
            jump behind_bleachers_day_four
        "To the bandroom":
            jump clubroom_day_four

                                ################
                                #SKELETON DAY 4#
                                ################
label gym_day_four:
    scene gym
    show mc at left
    "The gym smells like wet stone and fermented broccoli. Cal is pumping a weight on a bench. He's filled with determination" 
    show sk at right
    sk "HEY BROMEATMCMAN. How's life"
    mc "Good, good. Are you getting ready for Halloween night?"
    sk "Fuck yeah dude. Took one too many drinks yesterday and I have to burn off the calories. Else it would go right to my ribs."
    mc "Well I hope that you feel good and fit for that"
    sk "Oh dude me too. A few of my pals and I have a competition to see how many people we can kill"
    mc "Who usually wins that?"
    menu:
        sk "Take a fucking guess"
        "You do":
            sk "Hell yeah I do"
            $ skeleton_sus += 10
            jump gym_day_four_end
        "A friend does": 
            sk "Really after all we've been through bro?"
            sk "I do, I do"
            $ skeleton_sus -= 10
            jump gym_day_four_end

label gym_day_four_end:
    sk "Last year I must've taken 6 dozen souls"
    mc "Impressive"
    sk "Yeah it is"
    mc "Do you ever try to talk to the humans before you, uh -"
    sk "Pull there spines out and wear it as a belt?"
    mc "Uh, yeah that."
    sk "Not really no. Humans are too pretentious for conversation"
    sk "But no one's too pretentious to have their bones be used as fashion accessories."
    sk "At the end of the day we find the person who had the largest foot and we play –"
    mc "Football?"
    sk "No, actually cricket"
    sk "You should come see me play, should be at 11 tonight"
    mc "Maybe I will"
    jump end_day_four

                            ###############
                            #BANSHEE DAY 2#
                            ###############
label clubroom_day_four:
    "Banshee walks in, looking more serious than usual."
    banshee " Seeing everyone so excited about killing is making me kinda sad."
    mc "Yeah it's kinda wild."
    "As long as I don't die I'm fine to be honest."
    banshee "Less humans means less happiness and less fans for my awesome band!"
    "Yeah. That's what's fucked about it."
    banshee "Anyway will you be coming to see me tonight?"
    menu:
        "Yeah of course.":
            jump club_day_four_good
        "Nope":
            jump club_day_four_bad

label club_day_four_good:
    banshee "Good I’m glad."
    banshee "I'll see you tonight, [mc]!"
    "They smile brightly." 
    " I'm still not used to it, and my face flushes with red."
    mc "I'm looking forward to it."
    $ banshee_sus -=40
    jump end_day_four

label club_day_four_bad:
    banshee "Well hope you have fun. I prolly shouldn't be around anyone anyway."
    $ banshee_sus +=40
    jump end_day_four

                                ##############
                                #ZOMBIE DAY 4#
                                ##############
label behind_stairs_day_four:

    "When I reached Zoë's spot behind the stairs she jumped up to greet me."
        
    show zombie happy at right

    show mc at left

    zombie "[mc]! I've found him! I've found the human I've been looking for!"

    mc "Oh have you now? Who is it?"

    "She pulled out her phone and rapidly tapped on it. She shoved the phone in my face."

    mc "Melon Eluck? The guy who made Tlsea?"

    zombie "Yes!! His brain is amazing. All he does is post to Tweeter about how smart he is! According to the book, that means he is the best candidate!"

    mc "But how are you going to get to him? He's super rich and I'm sure he knows not to leave on Friday."

    show zombie at right

    zombie "Of course. He is the {i} one {/i} after all. I dmed him on Tweeter and told him he's too much of a coward to not go out tomorrow."

    "She showed me a conversation of her taunting and egging him on. The conversation ended with him declaring that he would create the best defense against monsters and would prove that it's the best by going for a stroll on tomorrow."

    mc "Wow, impressive."

    show zombie_happy at right

    zombie "I'm so excited for tomorrow!"
    python:
        if (zombie_sus > 50):
            renpy.jump(zombie_good_day)
        else:
            renpy.jump(zombie_bad_day)

label zombie_good_day:
    show zombie blushie at right

    zombie "So do you think you'll still be able to help me tomorrow? With your lightning magic?"

    show mc_blush at left

    mc "Oh yeah of course! Melon Elusk will never see it coming!"

    show zombie_happy at right

    zombie "Let's get that brain!"

    jump end_day_four

label zombie_bad_day:
    mc "Still need my lightning magic?"
    
    show zombie sus at right
        
    "Zoë gave me a look"

    zombie "Lightning magic, right. I think I'll get through it on my own."

    mc "Right. Of course. I'll see you tomorrow, I guess…"

    jump end_day_four


####### END DAY 4 ########
label end_day_four:

    "Who do you want to spend Halloween with?"

    menu:
        "Zoe":
            if zombie_sus > 50:
                jump behind_stairs_day_halloween_good
            else:
                jump behind_stairs_day_halloween_bad
        "Todd Howard":
            if windego_sus > 50:
                jump behind_bleachers_day_halloween_good
                
            else:
                jump behind_bleachers_day_halloween_bad
        "Banshee":
            if banshee_sus > 50:
                jump clubroom_day_halloween_good
            else:
                jump clubroom_day_halloween_bad
        "Cal":
            if skeleton_sus > 50:
                jump gym_day_halloween_good
            else:
                jump gym_day_halloween_bad
#################################
#                               #
#       HALLOWEEN SCENES        #
#                               #
#################################

                        #########################
                        #SKELETON HALLOWEEN GOOD#
                        #########################
label gym_day_halloween_good:
    scene gym
    show mc at left
    show sk at right
    "From the window of the gym I see a group of skeletons on the field with a bat and wicket. The field seems to be burning, and be made of broken glass. I decide to stay inside. Cal is up to bat right now. I yell out:"
    mc "HEY BRO HOW'S IT GOING"
    sk "OH HEY WITCHYBROMEATMCGILLIGCUDY, did you hear?"
    mc "WHAT?"
    sk "I BROKE THE SCHOOL RECORD. 100 SOULS"
    mc "WOAH NICE"
    sk "YEAH HEY, THANKS FOR THE SUPPORT THIS WEEK"
    mc "NO PROBLEM"
    sk "ALSO I KNOW YOU'RE A HUMAN"
    mc "HA HA THAT'S GREAT BRO"
    mc "Wait, what the fuck"
    sk "YEAH, IT WAS PRETTY OBVIOUS"
    sk "BUT IT'S COOL"
    sk "I'M STILL GOING TO TAKE YOUR SOUL"
    sk "BUT NOT IN THE KILLING WAY. IN THE LOVE WAY"
    sk "DO YOU WANT TO BE MINE?"
    mc "YES"
    sk "GREAT"
    mc "COOL"
    sk "YES!"
    jump game_credits

                        ########################
                        #BANSHEE HALLOWEEN GOOD#
                        ########################
label clubroom_day_halloween_good:
    
    scene clubroom

    "I meet banshee in front of the club rom and we walk to their house."
    banshee "It’s just you and me. Hope that’s okay."
    "I nod uneasily and follow them inside.It’s comfy here and there are records everywhere." 
    banshee "I have a surprise for you!! Sit! I'll be right back."
    " I sit on the floral couch and wait for them to come back. When they do they’re holding an acoustic guitar."
    banshee "I wrote this for you. I know I said today makes me sad, but you make me happy." 
    banshee "I hope you like it!"
    "My heart stills as a soft, lovely melody starts to play and banshee sings in voice I’ve never heard before. A voice so differently from the usual startling boom."
    "The song is too beautiful.It’s about them and me and the magic of love and wanting to be human."
    "It's about knowing I am."
    mc "You know?"
    "Banshee nods."
    mc "I’m sorry."
    banshee "Dont be. You were trying to keep yourself safe."
    banshee "I want you to be safe."
    "Banshee sets the guitar down."
    banshee "Did you like the song?"
    "Their voice is loud again, but I'm used to it by now." 
    "I like it."
    "I like Banshee."
    mc "Of course I do."
    "I smile, still warm from being serenaded."
    mc "I like you."
    jump game_credits

                    #######################
                    #ZOMBIE HALLOWEEN GOOD#
                    #######################
label behind_stairs_day_halloween_good:
    
    scene hallway
    
    show zombie at right

    show mc at left

    "Zoë and I spend the night chasing after Melon Elusk. His grand plan was to drive around his Tlsea and glued some spikes to it. SOmething straight out of Max Mad. With the help of some "magic" from me and knowledge from Zoë, he didn't stand a chance."

    zombie "Hey, you want some?"

    "Zoë held out a piece of the cerebellum. I tried not to gag."

    mc "No, I'm good. That's all you."

    "When she finished munching on his brain meats, she stood up and hugged me."

    zombie "Thank you so much for helping me. Must have been hard since you're also a human and all."

    mc "I uh- No! I'm a Witch! You've seen my magic!"

    "Zoë laughed."

    zombie "After absorbing his knowledge I learned what human \"magic\" is and what a taser is. I know you're human, [mc]."

    mc "I, uh, okay. Are you gonna… eat me… now?"

    zombie "Of course not!"

    mc "Then uh.. what happens now..?"

    "Zoë blushed."

    zombie "Will you.. go out with me?"

    mc "Yes! Just don't eat my brain!"

    zombie "Never!"

    show zombie love at right

    show mc love at left

    jump game_credits

                        ########################
                        #WENDIGO HALLOWEEN GOOD#
                        ########################
label behind_bleachers_day_halloween_good:
    scene bleachers
    show mc at left
    show wendigo at right
    mc "Are you ready to go on the big Hunt?"

    wendigo "No… My parents want me to eat someone, but I'm {i} vegan {/i}. Why can't they understand that?"

    mc "Have you talked to them about it?"

    wendigo  "Yeah. If I just do this one thing, then they said they {i} might consider{/i} letting me be fully vegan."

    mc "Screw that."

    wendigo  "What?"

    mc "Screw that. Who cares what they think?"

    wendigo "But they're my parents…"

    mc "And? If they don't support you, then what kind of parents are they?"

    wendigo  "..."

    mc "Listen man, they'll come around eventually, but you can't keep jumping through hoops to appease them if it won't make you happy."

    wendigo  "You're right."

    "Todd Howard tapped a few things on his phone."

    show wendigo blushie at right

    wendigo "Do you want to go somewhere with me?"

    show mc blushie at left

    mc "Uh.. sure where?"

    wendigo "There's this really good restaurant not too far from here."

    mc "Let's go."

    "Together, the two of us go and share a meal. A vegan meal."

    show mc love at left

    show wendigo love at right 

    jump game_credits 

#####
#BAD#
#####


                        ########################
                        #SKELETON HALLOWEEN BAD#
                        ########################
label gym_day_halloween_bad:
    "I walk out to the gym. The lights are off. I go find the switch."
    scene Gym
    show sk
    sk "Hey bro"
    sk "Bad news"
    sk "I tied with my friend."
    mc "Damn that really sucks"
    sk "Yeah I know"
    sk "I just needed one more human's soul"
    sk "There has to be one more"
    sk "And then I realized"
    sk "I've been talking to one all week"
    mc "How'd you find out?"
    sk "I knew this was too good."
    sk "I don't really get close to people."
    sk "They say I'm {i}toxic{/i}"
    sk "You got too close"
    sk "Then I knew"
    sk ""
    sk "..."
    sk "Sorry bro"
    jump game_credits

                        #######################
                        #BANSHEE HALLOWEEN BAD#
                        #######################
label clubroom_day_halloween_bad:
    scene clubroom
    show mc at right
    show banshee at left
    mc "Hey!"
    banshee "Hi."
    "I meet Banshee after class in the club room, but something feels off."
    "Banshee won’t look at me."
    mc "What’s wrong friend?"
    banshee "Are you serious right now?"
    mc "I don’t understand."
    banshee "You’re a human!"
    mc "What? No. I'm a witch remember."
    banshee "You’re a human. You can’t do real magic! Everything you’ve told me in a lie."
    "Tears are streaming down Banshee's face." 
    mc "I-"
    banshee "I trusted you!"
    mc "I’m sorry I’m so sorry really I just wanted-"
    "The wailing starts and my vision fades before it stops."
    banshee "I didn’t mean to [mc]."
    banshee "I’m so so sorry."
    jump game_credits

                        ######################
                        #ZOMBIE HALLOWEEN BAD#
                        ######################
label behind_stairs_day_halloween_bad:
    scene hallway
    show zombie at right
    show mc at left
    zombie "Before we go I need to tell you something."

    mc "What's up?"

    zombie "I know you're not a Witch."

    mc "I-"

    zombie "I know you're human."

    mc "No- I-"

    "Before [main] could respond Zoë jumped on them and ate his brain meats. She didn't learn too much, but she did learn some sweet magic tricks. Using this knowledge she was able to easily over power Melon Elusk." 

    jump game_credits

                        #######################
                        #WENDIGO HALLOWEEN BAD#
                        #######################
label behind_bleachers_day_halloween_bad:
    scene bleachers
    show wendigo at right
    show mc at left
    
    wendigo "[main], I know you've been hiding something from all of us."

    mc "What do you mean?"

    wendigo "You're not a Witch, you're just a human who's playing pretend."

    mc "What? No that's crazy talk. Look."

    "I pull small firecrackers and throw them to the gound."

    mc "See? Magic! I made sparks."

    "He shook his head."

    wendigo "Just more magic tricks created by humans."

    "He pulled out his phone and showed me an Instagram account. It was a human magician account. My heart sank."

    mc "Todd, listen man, I can explain-"

    wendigo "I'm sorry. I wish things could have turned out differently."

    "Before could respond, Todd grabbed me took and a photo of us together."

    wendigo "My parents don't believe in my veganism, so I have to show them that I can eat humans, I just don't want to. Maybe then they'll see there's nothing wrong with me."

    mc "Todd…"

    wendigo "I'm sorry [mc]. I don't want to do this any more than you don't want it to happen."

    "Todd proceed to eat [mc], gagging and crying as he did so. [mc] begged and pleaded but Todd didn't stop. He had to."

    wendigo "I'm sorry."

    jump game_credits


################################
# # # # # GAME CREDITS # # # # #
################################
label game_credits:
    "Credits:"
    show wendigo at right
    show sk at left
    show teacher at center
    "Angel Ortiz: Character Art"
    scene hallway
    show zombie
    "Cam Perry: Zoë Branch & Lead Programmer"
    scene gym
    show sk
    "Elijah Cobb: Cal Branch & QA Testing & Lead Programmer"
    scene classroom
    show teacher at left
    show wendigo at right
    "Jamie Camera: Classrooms and Todd Branch & Lead Programmer"
    hide teacher at left
    hide wendigo at right
    show zombie at left
    show banshee at right
    show mc at center
    "Katt McCann - Character Art"
    scene clubroom
    "Maddy Marzano - Backgrounds"
    show banshee
    "Tulani Reeves-Miller Background Art and Story"
    scene black
    "Thank you so much for playing our game"
    jump end_game





label end_game:
    # This ends the game.
    return

