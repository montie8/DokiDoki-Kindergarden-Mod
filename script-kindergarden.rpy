label kindergarden_main:

    $ mse_name = "Miss Emiko"
    $ npc_name = "Receptionist"
    $ bs_name = "Sayori"
    $ bm_name = "Monika"
    $ bn_name = "Natsuki"
    $ by_name = "Yuri"
    
    scene bg sayori_bedroom
    with dissolve_scene_full
    show sayori 2t zorder 2 at t11
    s "[Player]...? Why did you do this to us? Why?"
    s 2u "Please..."
    s "Don't let it happen again."
    s 3f "Save them."
    s 4w "SAVE."
    s "THEM."
    
    scene bg bedroom 
    with 
    play music k1 

    $ restore_all_characters()
    
    "That's the third one this week..."
    "These messed up reocurring dreams are starting to get to me."
    "I've never seen anybody looking like that before, who even are they?"
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

    "Once I had finally found it, I entered the class, noticing the teacher, who i presumed to be Miss Emiko."
    "She had short blonde hair in a half bun, and she wore professional neat clothes."
    "She looked around 20-25 years old.
    ms_e "Hi, are you the new EA?"
    mc "Yeah, I am. I'm guessing you're Miss Emiko?"
    ms_e "Yup! Here you'll do tasks like, individually helping children, setting up activites, marking work, and that kind of thing."
    mc "Okay, where are all the kids though? It's a weekday, right?"
    "Miss Jones chuckled, then begin to speak."
    ms_e "They're at their music lesson right now."
    ms_e "They stay in the same classroom all day except for special activities, such as computer, music, sport, and all that."
    ms_e "It's a nice time to relax and be in peace and quiet, ahah!"
    "Miss Emiko seemed quite friendly and kind. I laughed back at her joke, and started doing some training work."
    "I started by marking some of the student's maths work, which was quite tedious, but it'd be worth it."
    "Soon, I hear the sounds of children giggling and running over to the classroom."
    "I assume that'd be the students."
    
    # The 4 girls enter 
    # have each girl go up a zorder

    ms_e "Hello everyone! How was music?"

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
    ms_e "This is Yuri,"

    show yuri 1k zorder 1 at s44
    show sayori 1k zorder 3 at f21    
    
    ms_e "Sayori,"

    show sayori 1k zorder 1 at s41
    show natsuki 1k zorder 3 at f32

    ms_j "Natsuki,"
    
    show natsuki 1k zorder 1 at s43
    show monika 1k zorder 3 at f32
    
    ms_e "And Monika!"

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
    ms_e "Soon Sayori, be patient."

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
    ms_e "That's a good question..."
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

    ms_j "Everything going alright, [player]?"
    mc "Yeah, It's nothing."
    "I quickly smile at her, while walking towards Yuri"
    mc "Hi Yuri, what are you reading?"
    "She's silent."

    "She didn't notice me."
    "I softly repeat my question." 
    
    by "O-oh! Hi..."
    "She seemed rather startled by my sudden appearance."
    by "This novel is named {i}'Moving Towards Time'{/i}."
    by "It's a book with very deep meanings, like the good guy can turn back time.."
    by "He uses his ability to help the police investigate through many cases, oftenly leading to saving the city..."
    by "But one da..."

    "Yuri looks like she just realized she said something wrong."
    "Immediatly after that she starts whispering to herself"

    by "I-I'm such an idiot..."
    mc "Hey, don't say that! You did nothing wrong!"
    by "But I just- J-just spoiled the whole b-book..."
    "Yuri's face starts to go red, she seems as if she's about to cry."
    mc "That doesn't mean you have to say mean things about yourself!"
    "She looks at me with her purple eyes full of tears"
    by "{i}*sigh*{/i} H-how do you k-know that...?"
    "She looked up at me with hope, a puddle of water on her desk where she sat."
    mc "I am sure, now wipe away those tears, let's read your book"
    mc "You're so mature and clever Yuri, nobody deserves to feel upset, especially you."

    "Mis Emiko looks impressed by the fact that I easily calmed down Yuri."
    "Mom might've thought right that I know my way with kids."
    "I gently take Yuri to sit on my lap for us to find a nice spot where to read."
    "We decided to sit down outside, on the bench."
    
    # switch bg here, to some outside thing
    
    "Then we began."
    "We continue like that for almost ten minutes."
    "Wow, just wow,"
    "The book was quite mature for a kindergartener, Yuri was definetely unique."

    ms_e "[player]? I need some help..."
    mc "I have to go, It was nice reading with you Yuri.""
    by "Really?"
    "She looks at me with the happiest face I ever saw."
    mc "It was awesome! I can't wait to read with you the next time!"
    "What a book..."
    "I stand up and walk up to Miss Emiko, ready for my next task."
    ms_e "[player], I can't find Sayori. Can you please look for her?"
    mc "Sure, Where'd you last see her?"
    ms_e "She said she is going to the class next to us for the pencils."
    ms_e "She doesn't know her way around school very well, I'm afraid she may have gotten lost..."
    mc "Alright, I'll find her."

    "Time to find a Sayori..."
  
    "To be continued"
    
    return

label kindergarden_sayori:
    "Sayori Route Coming Soon... "
    
    return
