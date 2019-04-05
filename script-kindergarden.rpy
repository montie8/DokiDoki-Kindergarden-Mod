label kindergarden_main:

    $ msj_name = "Miss J"
    $ npc_name = "???"
    $ bs_name = "Sayori"
    $ bm_name = "Monika"
    $ bn_name = "Natsuki"
    $ by_name = "Yuri"

    scene bg bedroom 
    with dissolve_scene_full
    play music k1 

    $ restore_all_characters()

    "That's the third one this week..."
    "These messed up reocurring dreams are starting to get to me."
    "I guess it's made me realise how unstructured my life is."
    "They say a job will keep you occupied, but what would I even do?"
    "I'm way too weak for heavy- or even light labor."
    "Although, my mom did always say I was good with kids."
    "And well, there is a kindergarten hiring nearby."

    stop music fadeout 1.0

    
    scene bg closet #scene bg cafe
    with wipeleft_scene

    "It's been a few days since I filled out the interview for a teacher helper at the kindergarten."
    "They're supposed to contact me sometime this week, to let me know if I'm hired or not."
    "Today I was out at a cafe with some friends, we were just hanging out, catching up, all that."
    "And it's going well till I'm interrupted by a phone call."
    "I excuse myself from the table and head outside the cafe to answer it."
    
    scene bg house #bg outside cafe
    with wipeleft_scene

    npc "Hi, this is [player], correct?"
    mc "Yes, it is."
    npc "Great. I've called you to let you know you've been accepted as an EA at Kinglow Primary."
    "I mouthed a 'Yes!' to myself as I grinned excitedly."
    mc "That's great to hear!"
    npc "Your first shift is on Monday, 9am. See you there."
    mc "Alright, bye."
    "I hung up the phone and walked back to my seat, smiling uncontrollably."
    "I boasted to my friends about the new job, and finished eating."

    scene bg kitchen
    with wipeleft_scene

    "Before I knew it, it was already Monday."
    "I woke up early and got dressed, eating breakfast."
    "I've never been this excited to go to work."
    "Heading out the door, I drove into the parking lot of Kinglow Primary."

    
    scene bg corridor #scene bg school outside 
    with wipeleft_scene

    "The building was rather large for a primary school..."
    "Kinglow Primary... Heh.."
    "The name is nice, it just slides off your tongue."

    
    scene bg club_day #scene bg inside of school
    with wipeleft_scene

    "I entered the building, the smell of fresh air conditioning and strong perfume drifted around me."
    "I first noticed a lady sitting at the desk, she calmly lifted her head, looking up at me."
    npc "Hello! You must be [player]."
    mc "Yeah, I am. I'm here as an EA...?"
    npc "Yes, you'll be working with Miss Jones in KM1."
    mc "Thank you."
    "I wandered around the nicely decorated building, looking for a class labeled KM1."

    scene bg class_day
    with wipeleft_scene

    "Once I had finally found it, I entered the class, noticing the teacher, who i presumed to be Miss Jones."
    "She had short blonde hair in a half bun, and she wore professional neat clothes."
    "She looked around 20-25 years old.
    (Her full name is Miss Jones, but i'll just write ms j, cause it's easier."
    ms_j "Hi, are you the new EA?"
    mc "Yeah, I am. I'm guessing you're Miss Jones?"
    ms_j "Yup! Here you'll do tasks like, individually helping children, setting up activites, marking work, and that kind of thing."
    mc "Okay, where are all the kids though? It's a weekday, right?"
    "Miss Jones chuckled, then begin to speak."
    ms_j "They're at their music lesson right now."
    ms_j "They stay in the same classroom all day except for special activities, such as computer, music, sport, and all that."
    ms_j "It's a nice time to relax and be in peace and quiet, ahah!"
    "Miss Jones seemed quite friendly and kind. I laughed back at her joke, and started doing some training work."
    "I started by marking some of the student's maths work, which was quite tedious, but it'd be worth it."
    "Soon, I hear the sounds of children giggling and running over to the classroom."
    "I assume that'd be the students."
    
    # The 4 girls enter 
    # have each girl go up a zorder

    ms_j "Hello everyone! How was music?"

    show yuri 1k zorder 2 at t44
    show natsuki 1k zorder 2 at t43
    show monika 1k zorder 2 at t42
    show sayori 1k zorder 2 at t41

    "I hear a jumble of 'Good!' 'Fun' and other opinions from the 4 girls."
    "It's suprising there's only 4, it's rather strange considering other schools nomally have around 20 students per class."
    "But I decide to ignore it anyway."
    ms_j "Children, this is our new friend, [player]!"
    "The girls smile at me."

    show yuri 1k zorder 3 at f22
    show natsuki 1k zorder 1 at s43
    show monika 1k zorder 1 at s42
    show sayori 1k zorder 1 at s41
    ms_j "This is Yuri,"

    show yuri 1k zorder 1 at s44
    show sayori 1k zorder 3 at f21    
    
    ms_j "Sayori,"

    show sayori 1k zorder 1 at s41
    show natsuki 1k zorder 3 at f32

    ms_j "Natsuki,"
    
    show natsuki 1k zorder 1 at s43
    show monika 1k zorder 3 at f32
    
    ms_j "And Monika!"

    hide monika
    hide natsuki
    hide sayori
    show yuri 1k zorder 3 at t11
    
    by "H-hi..."
    "The one that was apparently named Yuri, spoke softly and quietly. Her purple hair covering most of her face."

    show yuri 1k zorder 2 at s22
    show sayori 1k zorder 3 at t11

    bs "This is boooooringgg!"
    bs "Can we play some games?"
    ms_j "Soon Sayori, be patient."

    show yuri 1k zorder 2 at s44
    show sayori 1k zorder 2 at s22
    show natsuki 1k zorder 3 at t21

    bn "What's a pashent?"
    "Yuri held in a chuckle, trying not to laugh at Natsuki attempt."
    bn "What's so funny?!"
    by "N-nothing..."

    hide natsuki
    hide sayori
    hide yuri 

    "It took me a while to realise that Monika, the brown haired one was gone."
    mc "Where'd Monika go?"
    ms_j "That's a good question..."
    "After a quick glance around the room, I saw Monika in the corner reading a book, I walked up to her and crouched down."

    # cg here

    mc "Are you okay?"
    "She glanced up at me."
    bm "Yeah."
    mc "What're you reading?"
    "She simply turned the front of the book to me, keeping her mouth shut."
    " {i}'Coding for dummies'{/i} The title read."
    mc "Hm? You like coding?"
    "I was quite surprised somebody as young as her would be interested in that."
    "She nodded."
    bm "Do you like coding?..."
    mc "I mean, I've never tri-"
    bm "You should."
    "She spoke confidently but somehow a bit rudely."
    mc "Alright, I'll take it into consideration."

    # Space To Possibly

    # make scene longer

    # bg classroom

    "I didn't want to bother her anymore, so I stood up and went to join the others."
    "Although, I found that they had all split up to do their own activities."
    menu:
        "Who should I talk to first?"
        "Natsuki":
            call kindergarden_natsuki
        "Yuri":
            call kindergarden_yuri
        "Sayori":
            call kindergarden_sayori

    return

label kindergarden_natsuki:

    "I decide to go with Natsuki first."
    "I noticed her looking at one of the shared ipads they had in the classroom."
    "She sat at one of the desks, watching intensly."
    "I walked up to her to see what she'd been watching."
    "It was a cartoon."
    "The style was cute, almost like an anime but for kids."
    mc "Hey there, what're you watching?"
    bn "P-parfait Princesses series 11..."
    "She spoke so quietly I could barely hear her."
    mc "What was that?"
    bn "PARFAIT PRINCESSES SERIES 11! DO YOU EARS NOT WORK OR SOMETHING?!"
    "I was startled by her sudden anger."
    "Everybody in the room turned to look at us."
    bn "Hmph..."
    "She continued to watch the cartoon."
    mc "May I watch?"
    bn "You wont like it..."
    mc "Why don't you think I'd like it?"
    bn "It's for kids. Everybody wants to watch and do grown-up things..."
    mc "Well, you can like whatever you want to like."
    "I could see almost a spark appear in her eyes as a I said that."
    bn "I-if you want to watch you can."
    mc "Thank you."
    "I pulled a seat from another desk and sat myself next to her."
    mc "What's it about?"
    bn "Just watch to find out."
    mc "That's not very polite..."
    bn "Hmph..."
    mc "Do you do anything else other than watch this movie?"
    bn "It's a series, not a movie!"
    "She scolded me angrily, I obviously said something wrong there."
    mc "Sorry, what else do you do other than watch this series?"
    bn "I like to help mommy make cookies..."
    mc "Hm? Help mom make cookies?"
    "I smiled at the scene, it was adorable."
    bn "Y-yeah..."
    mc "That's nice of you."
    bn "Well, I would help her make cookies, but, I can't.."
    mc "Why is that?"
    "I assumed it'd be because they ran out of ingredients, or her mother was out of town."
    bn "She went away a while ago."
    bn "I don't know where she went, daddy said she went to go live in another house."
    bn "He didn't tell me why."
    bn "But when she went to go live somewhere else, daddy has been mean to me."
    bn "B-but don't tell anybody! He'd be really mad if i told anybody about it."
    bn "So pretend you heard nothing."
    "Holy shit."
    "I can't even believe what I just heard."
    "This was a whole new level of what the hell."
    "I just sat there staring into space, trying to process all this information."
    bn "Mister [player]? Are you okay?"
    "I was interrupted from my thoughts."
    mc "Yeah, I'm okay, thank you..."
    "Does this mean-"
    "No, I don't even want to think about it."
    "I need to tell Miss Jones."
    mc "I have to go do something, It was nice watching your cartoon with you, Natsuki!"
    n "Bye bye!"
    "She smiled innocently, that innocent smile was so adorable, but after hearing what she just said..."
    "It was more sinister than anything."

    "To Be Continue.."

    return

label kindergarden_yuri:

    "I decide to go look what's Yuri doing right now."
    "I found her pretty quickly, she was sitting by the wall reading a book."
    "Wait a minute,"
    "A book."
    "I guess this kindergarten is full of prodigies."

    ms_j "Everything ok mister [player]?"
    mc "Yes, i just thought of something, everything is fine."
    "I quickly smile at her, while walking towards Yuri"
    mc "Hi Yuri, what are you reading?"
    by "H-Hey."

    "She looks so startled by my arrival. I just hope she doesn't want to kill me now."
    "I softly repeat my question." 

    by "This novel is named {i}'Walking towards the time'{/i}."
    by "It's a book with very deep meanings, for example the main hero is an anomaly that can turn back the time."
    by "He uses his ability to help the police investigate through various cases, oftenly leading to solving it..."
    by "But one da..."

    "Yuri looks like she just realized she said something wrong."
    "Immediatly after that she starts whispering to herself"

    by "im such an idiot..."
    mc "Hey, don't say that! You did nothing wrong!"
    by "but i spoiled almost the whole book..."
    mc "That doesn't mean you have to say bad things about yourself"
    "She looks at me with her purple eyes full of tears"
    by "are you {i}*sigh*{/i} sure?"
    mc "I am sure, now wipe out your tears, let's read your book"

    "Mis Jones looks impressed by the fact that i easily calmed down Yuri."
    "Mom might thought right that im good with kids."
    "I gently take Yuri to sit on my lap for us to find a nice spot where to read."
    "Then we started."
    "We continue like that for almost ten minutes."
    "Wow, just wow,"
    "The book was pretty difficult for me so how about for four years old Yuri."

    ms_j "Mister [player]?"
    mc "I'm sorry, i have to go. It was nice reading with you."
    by "Really?"
    "She looks at me with the happiest face i ever saw."
    mc "It was awesome! I can't wait to read with you the next time!"
    "What a book..."
    ms_j "Mister [player], I can't find Sayori. Can you please look for her?"
    mc "Sure, i'm gonna find her."
    ms_j "She said she is going to the class next to us for the pencils."
    mc "Ok."

    "Time to find a kid ehehe-..."
  
    "To be continued"
    
    return

label kindergarden_sayori:
    "Sayori Route Coming Soon... "
    
    return
