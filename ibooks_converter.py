#This is a script for converting the ugly iBooks notes exports into a clean Markdown file

def convert_lines(text):
    if line in text == #(insert date and time format (see codecademy cheatsheets)):
        delete line
    elif line in text == Chaper + number format:
        add line (unless it already exists) & remove the page #
    #maybe not neccessary elif line == '\n':
        print('\n')
    else:
        add line (+add page number from the line above if possible)
    #see if I need to do anything to account 

example_text = '''
August 3, 2020
Foreword by Adam Grant, p. xiii
to be a great manager, you have to be a great coach

August 3, 2020
Foreword by Adam Grant, p. xv
Having worked for a few years with Google’s pioneering people analytics team, it became obvious to me that almost everything great in the

August 3, 2020
Foreword by Adam Grant, p. xv
company happened in teams. That was my pitch in the talk: start treating teams, not individuals, as the fundamental building block of the organization

August 3, 2020
Foreword by Adam Grant, p. xv
Excellent teams at Google had psychological safety (people knew that if they took risks, their manager would have their back). The teams had clear goals, each role was meaningful, and members were reliable and confident that the team’s mission would make a difference

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 11
He appreciated that each person had a different story and background

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 16
he made sure the team was communicating, that tensions and disagreements were brought to the surface and discussed, so that when the big decisions were made, everyone was on board, whether they agreed or not
'''

#convert_lines(example_text)

example_text_full = '''
August 3, 2020
Foreword by Adam Grant, p. xiii
to be a great manager, you have to be a great coach

August 3, 2020
Foreword by Adam Grant, p. xv
Having worked for a few years with Google’s pioneering people analytics team, it became obvious to me that almost everything great in the

August 3, 2020
Foreword by Adam Grant, p. xv
company happened in teams. That was my pitch in the talk: start treating teams, not individuals, as the fundamental building block of the organization

August 3, 2020
Foreword by Adam Grant, p. xv
Excellent teams at Google had psychological safety (people knew that if they took risks, their manager would have their back). The teams had clear goals, each role was meaningful, and members were reliable and confident that the team’s mission would make a difference

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 11
He appreciated that each person had a different story and background

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 16
he made sure the team was communicating, that tensions and disagreements were brought to the surface and discussed, so that when the big decisions were made, everyone was on board, whether they agreed or not

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 19
Bill Campbell was known for many things, but perhaps his most notable characteristic, his signature, was the hug

I wonder how much this simple action factored into the trust and respect that Bill had. If you’re going to let someone hug you, you’re definitely more likely to have then trust you

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 23
For companies to be successful, they must continually develop great products, and to do that they must attract smart creatives and build an environment where these employees can succeed at scale

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 23
critical, factor for success in companies: teams that act as communities, integrating interests and putting aside differences to be individually and collectively obsessed with what’s good for the company

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 24
All too often, internal competition takes center stage, and compensation, bonuses, recognition, and even office size and location become the ways to keep score. This is problematic: in such an environment, selfish individuals can beat altruistic ones.

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 27
Coaching is no longer a specialty; you cannot be a good manager without being a good coach

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 27
create a climate of communication, respect, feedback, and trust

August 3, 2020
Chapter 1: The Caddie and the CEO, p. 29
swearing in the workplace enhances morale

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 40
People are the foundation of any company’s success. The primary job of each manager is to help people be more effective in their job and to grow and develop. We have great people who want to do well, are capable of doing great things, and come to work fired up to do them. Great people flourish in an environment that liberates and amplifies that energy. Managers create this environment through support, respect, and trust. Support means giving people the tools, information, training, and coaching they need to succeed. It means continuous effort to develop people’s skills. Great managers help people excel and grow. Respect means understanding people’s unique career goals and being sensitive to their life choices. It means helping people achieve these career goals in a way that’s consistent with the needs of the company. Trust means freeing people to do their jobs and to make decisions. It means knowing people want to do well and believing that they will.

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 58
THE THRONE BEHIND THE ROUND TABLE THE MANAGER’S JOB IS TO RUN A DECISION-MAKING PROCESS THAT ENSURES ALL PERSPECTIVES GET HEARD AND CONSIDERED, AND, IF NECESSARY, TO BREAK TIES AND MAKE THE DECISION

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 61
LEAD BASED ON FIRST PRINCIPLES DEFINE THE “FIRST PRINCIPLES” FOR THE SITUATION, THE IMMUTABLE TRUTHS THAT ARE THE FOUNDATION FOR THE COMPANY OR PRODUCT, AND HELP GUIDE THE DECISION FROM THOSE PRINCIPLES.

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 65
MANAGE THE ABERRANT GENIUS ABERRANT GENIUSES—HIGH-PERFORMING BUT DIFFICULT TEAM MEMBERS—SHOULD BE TOLERATED AND EVEN PROTECTED, AS LONG AS THEIR BEHAVIOR ISN’T UNETHICAL OR ABUSIVE AND THEIR VALUE OUTWEIGHS THE TOLL THEIR BEHAVIOR TAKES ON MANAGEMENT, COLLEAGUES, AND TEAMS.

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 66
MONEY’S NOT ABOUT MONEY COMPENSATING PEOPLE WELL DEMONSTRATES LOVE AND RESPECT AND TIES THEM STRONGLY TO THE GOALS OF THE COMPANY.

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 70
INNOVATION IS WHERE THE CRAZY PEOPLE HAVE STATURE THE PURPOSE OF A COMPANY IS TO BRING A PRODUCT VISION TO LIFE. ALL THE OTHER COMPONENTS ARE IN SERVICE TO PRODUCT

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 72
HEADS HELD HIGH IF YOU HAVE TO LET PEOPLE GO, BE GENEROUS, TREAT THEM WELL, AND CELEBRATE THEIR ACCOMPLISHMENTS

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 76
Who should be on the board? Smart people with good business expertise who care deeply about the company and are genuinely interested in helping and supporting the CEO

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 34
These engineers liked being managed, as long as their manager was someone from whom they could learn something, and someone who helped make decisions

This is the positive role of managers in a company — mentor ship and structure.

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 35
when a company is in the implementation stage of an innovation (such as when Google was developing its search engine and AdWords), they need managers to help coordinate resources and resolve conflicts

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 35
creativity flourishes in environments, such as Broadway shows, that are more network-oriented than hierarchical

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 35
Silicon Valley people can get off track, chasing other goals beyond running a good operation

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 36
adopted performance-oriented management techniques, such as monitoring, targeting, and incentives, performed much better than other plants

^ the firms that...

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 36
Listen. Pay attention

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 36
when direct reports are told to do something, they don’t necessarily respond. In fact, the more talented the subordinate, the less likely she is to simply follow orders.” A manager’s authority, she concludes, “emerges only as the manager establishes credibility with subordinates, peers, and superiors.”4

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 36
people don’t just chafe against an authoritarian management style, but are also more likely to leave the team altogether!

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 37
your title makes you a manager; your people make you a leader.”

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 37
You need to project humility, a selflessness, that projects that you care about the company and about people.”

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 40
company’s people should be treated as an asset

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 42
Great coaches lie awake at night thinking about how to make you better

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 42
THE TOP PRIORITY OF ANY MANAGER IS THE WELL-BEING AND SUCCESS OF HER PEOPLE

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 44
get everyone involved in the meeting from the outset in a fun way

Do a “Trip report” — just ask everyone what one fun or interesting thing they did each eeek

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 44
direct correlation between fun work environments and higher performance

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 45
“get the 1:1 right” and “get the staff meeting right” are tops on the list of his most important management principles

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 46
team meetings are a terrific opportunity to engage people, with one 2013 study concluding that the relevance of the meeting, giving everyone a voice, and managing the clock well are key factors to achieving that engagement

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 47
there were always five words written on the whiteboard, indicating the topics to discuss that day. The words might be about a person, a product, an operational issue, or an upcoming meeting. That’s how they organized their talk

When holding a 1V1, prepare your top 5 items but hold them back and ask for the other person to say their top 5 first (avoid groupthink)

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 48
see where there was overlap and make sure to cover those topics

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 48
having

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 48
these sort of “substantive” conversations, as opposed to truly small talk, makes people happier

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 49
What do your teammates think of you? That’s what’s important!

^ more important than your boss

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 52
BILL’S FRAMEWORK FOR 1:1s AND REVIEWS PERFORMANCE ON JOB REQUIREMENTS Could be sales figures Could be product delivery or product milestones Could be customer feedback or product quality Could be budget numbers RELATIONSHIP WITH PEER GROUPS (This is critical for company integration and cohesiveness) Product and Engineering Marketing and Product Sales and Engineering MANAGEMENT/LEADERSHIP Are you guiding/coaching your people? Are you weeding out the bad ones? Are you working hard at hiring? Are you able to get your people to do heroic things? INNOVATION (BEST PRACTICES) Are you constantly moving ahead . . . thinking about how to continually get better? Are you constantly evaluating new technologies, new products, new practices? Do you measure yourself against the best in the industry/world?

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 54
politics

Create an environment where everyone can share their ideas freely and the best ones win — not the ones who can convince the managers

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 54
that the goal of consensus leads to “groupthink” and inferior decisions

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 54
The way to get the best idea, he believed, was to get all of the opinions and ideas out in the open, on the table for the group to discuss. Air the problem honestly, and make sure people have the opportunity to provide their authentic opinions, especially if they are dissenting

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 55
when it is called a debate rather than a disagreement, participants are more likely to share information

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 56
when she was discussing a decision with her team, she always had to be the last person to speak. You may know the answer and you may be right, he said, but when you just blurt it out, you have robbed the team of the chance to come together. Getting to the right answer is important, but having the whole team get there is just as important

August 3, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 57
If you have the right conversation, Bill counseled, then eight out of ten times people will reach the best conclusion on their own. But the other two times you need to make the hard decision and expect that everyone will rally around it.

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 58
it’s the leader’s job, when faced with a tough decision, to describe and remind everyone of those first principles

Because first principles are universally accepted, it’ll help the two opposing sides to find common ground

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 67
“The purpose of a company is to take the vision you have of the product and bring it to life,” he said once at a conference. “Then you put all the other components around it—finance, sales, marketing

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 68
if you have the right product for the right market at the right time, go as fast as you can

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 69
Bill liked to tell a story about when he was at Intuit and they started getting into banking products. They hired some product managers with banking experience. One day, Bill was at a meeting with one of those product managers, who presented his engineers with a list of features he wanted them to build. Bill told the poor product manager, if you ever tell an engineer at Intuit which features you want, I’m going to throw you out on the street. You tell them what problem the consumer has. You give them context on who the consumer is. Then let them figure out the features. They will provide you with a far better solution than you’ll ever get by telling them what to build.

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 70
execs need to be able to talk to the engineers, even if they aren’t engineering execs

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 71
letting people go is a failure of management, not one of any of the people who are being let go

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 71
So it is important for management to let people leave with their heads held high

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 71
treating the departing people well is important for the morale and well-being of the remaining team

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 71
“Many of the people whom you lay off will have closer relationships with the people who stay than you do

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 72
When you fire someone, you feel terrible for about a day, then you say to yourself that you should have done it sooner. No one ever succeeds at their third chance.

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 73
Bill Campbell knew how to have fun. He made every table the kids’ table

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 74
the CEO manages the board and board meetings, not the other way around.*23 Board meetings fail when the CEO doesn’t own and follow her agenda. That agenda should always start with operational updates: the board needs to know how the company is doing. That includes financial and sales reports, product status, and metrics around operational rigor (hiring, communications, marketing, support). If the board has committees, for example to oversee audit and finance or compensation, have those committees meet ahead of time (in person or via phone or video conference) and present updates at the board meeting

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 74
The first order of business always needs to be a frank, open, succinct discussion about how the company is performing

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 75
Send out financial and other operational details ahead of time and expect board members to review them and come with questions

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 76
A company that is honest with its board can be honest with itself, too; people learn that not only is it okay to frankly share bad news, it’s expected

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 76
we would not include the highlights and lowlights in the packet of information that we sent to board members ahead of the meeting

August 5, 2020
Chapter 2: Your Title Makes You a Manager. Your People Make You a Leader., p. 77
bad board member looks like: “Someone who just walks in and wants to be the smartest guy in the room and talks too much.”

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 89
ONLY COACH THE COACHABLE THE TRAITS THAT MAKE A PERSON COACHABLE INCLUDE HONESTY AND HUMILITY, THE WILLINGNESS TO PERSEVERE AND WORK HARD, AND A CONSTANT OPENNESS TO LEARNING

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 92
PRACTICE FREE-FORM LISTENING LISTEN TO PEOPLE WITH YOUR FULL AND UNDIVIDED ATTENTION—DON’T THINK AHEAD TO WHAT YOU’RE GOING TO SAY NEXT—AND ASK QUESTIONS TO GET TO THE REAL ISSUE

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 97
NO GAP BETWEEN STATEMENTS AND FACT BE RELENTLESSLY HONEST AND CANDID, COUPLE NEGATIVE FEEDBACK WITH CARING, GIVE FEEDBACK AS SOON AS POSSIBLE, AND IF THE FEEDBACK IS NEGATIVE, DELIVER IT PRIVATELY

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 99
DON’T STICK IT IN THEIR EAR DON’T TELL PEOPLE WHAT TO DO; OFFER STORIES AND HELP GUIDE THEM TO THE BEST DECISIONS FOR THEM

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 103
BE THE EVANGELIST FOR COURAGE BELIEVE IN PEOPLE MORE THAN THEY BELIEVE IN THEMSELVES, AND PUSH THEM TO BE MORE COURAGEOUS

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 105
FULL IDENTITY FRONT AND CENTER PEOPLE ARE MOST EFFECTIVE WHEN THEY CAN BE COMPLETELY THEMSELVES AND BRING THEIR FULL IDENTITY TO WORK

August 5, 2020
Chapter 3: Build an Envelope of Trust, p. 79
When the board got together to discuss what to do about it, most of its members were willing to tolerate missing short-term financial targets, as they felt it was more important for the company to invest in the future. Short-term objectives weren’t as important as long-term growth, which might be sacrificed if spending was curtailed. Bill disagreed. He wanted to get leaner and make the numbers. That is the culture we want to have around here, he explained. It wasn’t so much about hitting those short-term numbers, but about creating a culture where anything less than operational excellence wouldn’t be tolerated

August 5, 2020
Chapter 3: Build an Envelope of Trust, p. 80
Perhaps the most important currency in a relationship—friendship, romantic, familial, or professional—is trust

August 5, 2020
Chapter 3: Build an Envelope of Trust, p. 83
Build trust first

Do you can have healthy task conflict without having it bleed into relationship conflict

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 84
the best teams are the ones with the most psychological safety

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 87
Coaches need to learn how self-aware a coachee is; they need to not only understand the coachee’s strengths and weaknesses, but also understand how well the coachee understands his or her own strengths and weaknesses

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 88
To be coachable, you need to be brutally honest, starting with yourself

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 90
Bill would never tell me what to do,” says Ben Horowitz. “Instead he’d ask more and more questions, to get to what the real issue was

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 91
When you listen to people, they feel valued

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 94
never embarrass someone publicly

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 94
I’ll give constructive feedback as soon as I can, but only when the person is feeling safe

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 100
it’s a manager’s job to push the team to be more courageous

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 101
be the person who gives energy, not one who takes it away

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 101
trust my instincts

August 7, 2020
Chapter 3: Build an Envelope of Trust, p. 104
People prefer leaders who are different because it makes leadership seem more attainable

August 10, 2020
Chapter 4: Team First, p. 115
WORK THE TEAM, THEN THE PROBLEM WHEN FACED WITH A PROBLEM OR OPPORTUNITY, THE FIRST STEP IS TO ENSURE THE RIGHT TEAM IS IN PLACE AND WORKING ON IT.

August 11, 2020
Chapter 4: Team First, p. 123
PICK THE RIGHT PLAYERS THE TOP CHARACTERISTICS TO LOOK FOR ARE SMARTS AND HEARTS: THE ABILITY TO LEARN FAST, A WILLINGNESS TO WORK HARD, INTEGRITY, GRIT, EMPATHY, AND A TEAM-FIRST ATTITUDE

August 11, 2020
Chapter 4: Team First, p. 124
PAIR PEOPLE PEER RELATIONSHIPS ARE CRITICAL AND OFTEN OVERLOOKED, SO SEEK OPPORTUNITIES TO PAIR PEOPLE UP ON PROJECTS OR DECISIONS

August 11, 2020
Chapter 4: Team First, p. 131
GET TO THE TABLE WINNING DEPENDS ON HAVING THE BEST TEAM, AND THE BEST TEAMS HAVE MORE WOMEN

August 11, 2020
Chapter 4: Team First, p. 134
SOLVE THE BIGGEST PROBLEM IDENTIFY THE BIGGEST PROBLEM, THE “ELEPHANT IN THE ROOM,” BRING IT FRONT AND CENTER, AND TACKLE IT FIRST

August 11, 2020
Chapter 4: Team First, p. 137
DON’T LET THE BITCH SESSIONS LAST AIR ALL THE NEGATIVE ISSUES, BUT DON’T DWELL ON THEM. MOVE ON AS FAST AS POSSIBLE

August 11, 2020
Chapter 4: Team First, p. 141
WINNING RIGHT STRIVE TO WIN, BUT ALWAYS WIN RIGHT, WITH COMMITMENT, TEAMWORK, AND INTEGRITY

August 11, 2020
Chapter 4: Team First, p. 144
LEADERS LEAD WHEN THINGS ARE GOING BAD, TEAMS ARE LOOKING FOR EVEN MORE LOYALTY, COMMITMENT, AND DECISIVENESS FROM THEIR LEADERS.

August 11, 2020
Chapter 4: Team First, p. 152
PERMISSION TO BE EMPATHETIC LEADING TEAMS BECOMES A LOT MORE JOYFUL, AND THE TEAMS MORE EFFECTIVE, WHEN YOU KNOW AND CARE ABOUT THE PEOPLE

August 10, 2020
Chapter 4: Team First, p. 110
Teams are not successful unless every member is loyal and will, when necessary, subjugate their personal agenda to that of the team

August 10, 2020
Chapter 4: Team First, p. 111
Purpose, pride, ambition, ego: these are vital motivators as well and must be considered by any manager or coach

August 10, 2020
Chapter 4: Team First, p. 112
work the team, not the problem

August 10, 2020
Chapter 4: Team First, p. 116
Bill looked for four characteristics in people

August 10, 2020
Chapter 4: Team First, p. 116
The person has to be smart

August 10, 2020
Chapter 4: Team First, p. 116
The person has to work hard, and has to have high integrity. Finally, the person should have that hard-to-define characteristic: grit

August 11, 2020
Chapter 4: Team First, p. 118
when change happens, the priority has to be what is best for the team

August 11, 2020
Chapter 4: Team First, p. 120
It’s not what you used to do, it’s not what you think, it’s what you do every day

August 11, 2020
Chapter 4: Team First, p. 128
on the most effective teams everyone contributes rather than one or two people dominating discussions, people on those teams are better at reading complex emotional states, and . . . the teams have more women

August 11, 2020
Chapter 4: Team First, p. 136
He would always get to the heart of a problem, but in a positive way.9

August 11, 2020
Chapter 4: Team First, p. 136
positive leadership makes it easier to solve problems, so Bill would praise teams and people, give them a hug, and clap them on the shoulder to boost their confidence and comfort

August 11, 2020
Chapter 4: Team First, p. 139
it’s amazing what can be accomplished if you don’t care who gets the credit.

August 11, 2020
Chapter 4: Team First, p. 147
tension, the smoke to a problem’s fire

Look for tension

Identifying areas of tension is especially important for WAIm because clubs are like a house of cards — easily destructed through conflicts/drama/disinterest

August 11, 2020
Chapter 4: Team First, p. 150
LISTEN, OBSERVE, AND FILL THE COMMUNICATION AND UNDERSTANDING GAPS BETWEEN PEOPLE

August 11, 2020
Chapter 4: Team First, p. 150
led off the meetings by talking about personal stuff

August 11, 2020
Chapter 5: The Power of Love, p. 168
THE PERCUSSIVE CLAP CHEER DEMONSTRABLY FOR PEOPLE AND THEIR SUCCESSES.

Specifically when a new product is launched / prototype built.

August 11, 2020
Chapter 5: The Power of Love, p. 173
ALWAYS BUILD COMMUNITIES BUILD COMMUNITIES INSIDE AND OUTSIDE OF WORK. A PLACE IS MUCH STRONGER WHEN PEOPLE ARE CONNECTED

August 11, 2020
Chapter 5: The Power of Love, p. 177
HELP PEOPLE BE GENEROUS WITH YOUR TIME, CONNECTIONS, AND OTHER RESOURCES

August 11, 2020
Chapter 5: The Power of Love, p. 182
THE ELEVATOR CHAT LOVING COLLEAGUES IN THE WORKPLACE MAY BE CHALLENGING, SO PRACTICE IT UNTIL IT BECOMES MORE NATURAL

August 11, 2020
Chapter 5: The Power of Love, p. 157
Bill. He didn’t separate the human and working selves; he just treated everyone as a person: professional, personal, family, emotions . . . all the components wrapped up in one. And if you were one of his people, he cared about you fiercely and genuinely

August 11, 2020
Chapter 5: The Power of Love, p. 157
an organization full of the type of “companionate love” that Bill demonstrated (caring, affectionate) will have higher employee satisfaction and teamwork, lower absenteeism, and better team performance

August 11, 2020
Chapter 5: The Power of Love, p. 161
He acted the same way with the store associates as he did with the people on the Apple board

August 11, 2020
Chapter 5: The Power of Love, p. 161
get to know the families

Focus on remembering names and events to have an enjoyable conversation when you see the person again.

People bias towards those who care for them (or at least act like it)

August 11, 2020
Chapter 5: The Power of Love, p. 165
TO CARE ABOUT PEOPLE YOU HAVE TO CARE ABOUT PEOPLE: ASK ABOUT THEIR LIVES OUTSIDE OF WORK, UNDERSTAND THEIR FAMILIES, AND WHEN THINGS GET ROUGH, SHOW UP

August 11, 2020
Chapter 5: The Power of Love, p. 172
what matters most are the bonds between the people on the team, which are forged by caring for each other and the common good

August 11, 2020
Chapter 5: The Power of Love, p. 180
love the founders, and ensure they stay engaged in a meaningful way regardless of their operating role

August 11, 2020
Chapter 5: The Power of Love, p. 184
love

Have love for the people I’m working with

August 11, 2020
Chapter 6: The Yardstick, p. 189
great products and the teams that create them are at the core of a great company. Everything else should be in service to that core

August 11, 2020
Chapter 6: The Yardstick, p. 190
there are things we all care about as people—love, family, money, attention, power, meaning, purpose—that are factors in any business situation. That to create effective teams, you need to understand and pay attention to these human values.

Understand what motivates someone and find out to to provide them with it

August 11, 2020
Chapter 6: The Yardstick, p. 193
his own kind of yardstick. I look at all the people who’ve worked for me or who I’ve helped in some way, he would say, and I count up how many are great leaders now. That’s how I measure success.

All Excerpts From

Schmidt, Eric. “Trillion Dollar Coach.” HarperCollins, 2019-03-04. Apple Books.
This material may be protected by copyright.



Sent from my iPad
'''