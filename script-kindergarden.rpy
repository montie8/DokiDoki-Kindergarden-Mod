label kindergarden_main:

    $ mse_name = "Miss Emiko"
    $ npc_name = "Receptionist"
    $ bs_name = "???"
    $ bm_name = "Monika"
    $ bn_name = "Natsuki"
    $ by_name = "Yuri"

    $ restore_all_characters()

    
    scene bg sayori_bedroom
    with dissolve_scene_full
    play music k1 
    show sayori 2t zorder 2 at t11
    bs "[player]...? Why did you do this to us? Why?"

    show sayori 2u zorder 2 at t11
    s "Please..."
    s "Don't let it happen again."
    s "There's no hope for us in the future."
    s "You have to go back, you have to prevent this."

    show sayori 3f zorder 2 at t11
    s "Save them."

    show sayori 4w zorder 2 at t11
    s "SAVE."
    s "THEM."

    $ bs_name = "Sayori"

    stop music fadeout 1.0
    scene bg bedroom 
    with wipeleft_scene
  

    
    "That's the third one this week..."
    "These messed up reocurring dreams are starting to get to me."
    "I've never seen anybody looking like that before, who even are they?"
    "I guess it's made me realise how unstructured my life is."
    "They say a job will keep you occupied, but what would I even do?"
    "I'm way too weak for heavy- or even light labor."
    "Although, my mom did always say I was good with kids."
    "And well, there is a kindergarten hiring nearby."

    

    
    scene bg cafe_background # added background to the mod_content file
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
    
    "I entered the building, the smell of fresh air conditioning and strong perfume drifted around me."
    "I first noticed a lady sitting at the desk, she calmly lifted her head, looking up at me."
    npc "Hello! You must be [player]."
    mc "Yeah, I am. I'm here as an EA...?"
    npc "Yes, you'll be working with Miss Emiko in KM1."
    mc "Thank you."
    "I wandered around the nicely decorated building, looking for a class labeled KM1."

    scene bg class_day
    with wipeleft_scene

    "Once I had finally found it, I entered the class, noticing the teacher, who i presumed to be Miss Emiko."
    "She had short blonde hair in a half bun, and she wore professional neat clothes."
    "She looked around 20-25 years old."
    ms_e "Hi, are you the new EA?"
    mc "Yeah, I am. I'm guessing you're Miss Emiko?"
    ms_e "Yup! Here you'll do tasks like, individually helping children, setting up activites, marking work, and that kind of thing."
    mc "Okay, where are all the kids though? It's a weekday, right?"
    "Miss Emiko chuckled, then begin to speak."
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
    ms_e "Children, this is our new friend, [player]!"
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

    ms_e "Natsuki,"
    
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
    "I watched her read for a bit, she seemed extremely focused, a feeling of determination in her eyes."
    "
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
    
    show natsuki 1k zorder 3 at t21
    
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
    
    # cg here
    
    mc "What's it about?"
    bn "Just watch to find out."
    mc "That's not very polite..."
    bn "Hmph..."
    mc "Do you do anything else other than watch this movie?"
    bn "It's a series, not a movie!"
    "She scolded me angrily, I obviously said something wrong there."
    mc "Sorry, what else do you do other than watch this series?"
    bn "I like to help daddy make cookies..."
    mc "Hm? Help dad make cookies?"
    "I smiled at the scene, it was adorable."
    bn "Y-yeah..."
    mc "That's nice of you."
    bn "Well, he doesn't like me."
    mc "Why is that?"
    "My mind began to fill with horrible possibilies that might be why she'd think her dad didn't like her..."
    bn "He's not very nice."
    bn "It doesn't matter though."
    bn "You wouldn't care."
    "A chill went down my spine."
    "It seemed like a touchy subject for her, and I didn't want to force her to explain more."
    mc "Alright then, don't feel like you can't tell me things, Natsuki."
    mc "I'm always here if you want to talk to me about anything."
    "She muttered out a small 't-thanks' and continued watching her show."
    "I quickly changed the topic."
    mc "So, what's your favourite school subject, Natsuki?"
    bn "Oh, I like to cook! And dance, it's fun."
    "Hearing her talk about her hobbies and giving that adorable honest smile made my heart melt."
    mc "Who taught you to cook?"
    bn "Uh... My mommy..."
    "Natsuki spoke anxiously, as if she was afraid to answer."
    mc "Is she a good cook?"
    bn "She {i}was{i/} a good cook..."
    "Oh boy... Here we go again."
    mc "I-it's alright, just calm down, let's talk about something else!"
    "I gave a nervous laugh and attempted to change the subject."
    bn "Ok then. Can we talk about Parfait Princesses?"
    mc "Of course.. Hah.. ha.."
    "For the next 10 minutes, I sat there pretending to listen to Natsuki ramble on and on about some kid's show."
    "Really, I was just scrolling through my phone, but she doesn't know that!"
    "Either way, she had fun explaining it to me, right?"
    mc "That's really cool! Although, unfortunately I have to go now."
    bn "Bye bye!"
    "She smiled a sweet, honest smile. It made me feel special, considering how rare it was for her to open up to people."

    return

label kindergarden_yuri:

    "I decide to go look what's Yuri doing right now."
    "I found her pretty quickly, she was sitting by the wall reading a book."
    "Wait a minute,"
    "A book."
    "I guess this kindergarten is full of prodigies."

    ms_e "Everything going alright, [player]?"
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
    "She looks at me with her glossy purple eyes full of tears"
    by "{i}*sigh*{/i} H-how do you k-know that...?"
    "She looked up at me with hope, a puddle of water on her desk where she sat."
    mc "I am sure, now wipe away those tears, let's read your book"
    mc "You're so mature and clever Yuri, nobody deserves to feel upset, especially you."

    "Mis Emiko looks impressed by the fact that I easily calmed down Yuri."
    "Mom might've thought right that I know my way with kids."
    "I gently take Yuri to sit on my lap for us to find a nice spot where to read."
    "We decided to sit down outside, on the bench."
    
    scene bg outside_school
    
    "Then we began."
    "We continue like that for almost ten minutes."
    "Wow, just wow,"
    "The book was quite mature for a kindergartener, Yuri was definetely unique."
    "I'm interrupted by Yuri nudging my arm a bit."
    by "H-hey, d-do you like it?"
    mc "Yeah, it's really good."
    "I nodded, giving her a shallow response."
    "I mean, she's like, 6 years old or something."
    "What do you expect me to do, give her an hour long full on book review?"
    "Yuri smiled faintly, flicking to the next page."
    by "That's good."
    by "A lot of the other kids make fun of me, I-I d-don't know why.."
    by "You're different..."
    "Small tears welled up in her eyes, but she was smiling at the same time."
    mc "Yuri, if anybody is being rude to you, you have to let a grown-up know."
    mc "It's not nice of them to do that."
    "I couldn't believe children would be cruel enough to bully poor Yuri."
    "I guess kids are brutal."
    by "Yeah, I k-know..."
    by "They said I c-cry too much, and that I'm like a baby."
    mc "Yuri, you're so mature and smart, don't listen to them!"
    "I wiped the tears from her eyes and closed the book to prevent it from getting wet."
    
    ms_e "[player]? I need some help..."
    mc "I have to go, It was nice reading with you Yuri."
    by "Really?"
    "She looks at me with the happiest face I ever saw."
    mc "It was awesome! I can't wait to read with you the next time!"
    by "Bye!"
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
