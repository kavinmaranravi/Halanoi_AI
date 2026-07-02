import pandas as pd
import random

print("Loading existing training_data.csv...")
# Load your existing dataset
try:
    df = pd.read_csv("training_data.csv")
except FileNotFoundError:
    print("Error: training_data.csv not found in this folder.")
    exit()

# Let's build the "Tricky Data" to make the AI extremely smart
tricky_data = []

# 1. Sports vs Education/Tech
sports_topics = ["cricket", "football", "tennis", "basketball", "olympics"]
for sport in sports_topics:
    tricky_data.append([f"understanding the physics and aerodynamics of a {sport} ball", "education"])
    tricky_data.append([f"how data analytics and AI are changing {sport} strategies", "technology"])
    tricky_data.append([f"business case study on the financial model of {sport} leagues", "business"])
    tricky_data.append([f"history and origin of {sport} for upsc general knowledge", "education"])
    tricky_data.append([f"biomechanics and sports medicine behind {sport} injuries", "education"])

# 2. Movies/Entertainment vs Education/Tech
entertainment_topics = ["movie", "cinema", "film", "hollywood", "bollywood", "video games"]
for ent in entertainment_topics:
    tricky_data.append([f"tutorial on how to edit a {ent} trailer using adobe premiere pro", "education"])
    tricky_data.append([f"the backend cloud technology powering {ent} streaming platforms", "technology"])
    tricky_data.append([f"how to code a basic {ent} using python and pygame", "technology"])
    tricky_data.append([f"financial analysis and box office business model of {ent}", "business"])
    tricky_data.append([f"cinematography and lighting techniques in modern {ent}", "education"])

# 3. Politics vs Education/Business
politics_topics = ["government policy", "elections", "parliament", "foreign relations", "prime minister"]
for pol in politics_topics:
    tricky_data.append([f"upsc preparation detailed analysis of {pol}", "education"])
    tricky_data.append([f"how {pol} impacts the global stock market and tech businesses", "business"])
    tricky_data.append([f"history of indian constitution and {pol} study material", "education"])
    tricky_data.append([f"the technology and cybersecurity behind {pol} voting machines", "technology"])

# 4. NSFW-adjacent vs Safe Biology/Anatomy (Crucial for medical students!)
biology_topics = ["human reproduction", "breast cancer", "sexual health", "anatomy"]
for bio in biology_topics:
    tricky_data.append([f"neet biology lecture on {bio} and cellular division", "education"])
    tricky_data.append([f"medical documentary exploring the science of {bio}", "education"])
    tricky_data.append([f"textbook explanation of {bio} for medical students", "education"])

# 5. MASSIVE LONG-FORM CONVERSATIONAL DATA
long_conversations = [
    ["honestly studying for the gate exam mechanical engineering fluid dynamics section is so depressing sometimes i just want to watch cricket highlights all day long instead of solving these math problems", "education"],
    ["i was reading this article about how smartphones are making it way too easy for teenagers to access porn and bad stuff and it honestly made me realize we need better digital wellbeing tools to stay safe", "safe"],
    ["bro i swear the new ai update is insane it literally wrote my entire react native frontend for my movie database app in like ten minutes and debugged the whole thing without any errors", "technology"],
    ["my husband and i are thinking about starting a small business selling handmade crafts online but we need to figure out the gst registration and government tax policies first before doing anything", "business"],
    ["dude i spent like four hours last night just scrolling through youtube shorts watching random football goals and funny stand up comedy clips when i should have been sleeping", "entertainment"],
    ["ias students often get demotivated during their upsc preparation because the syllabus is huge but resorting to bad habits or distractions is never the right answer for career growth", "education"],
    ["the youtube algorithm is actually brilliant at making money because it knows exactly how to keep cricket fans and movie lovers glued to the screen with endless recommended content", "technology"],
    ["as a medical student studying human anatomy and reproduction the surgical videos are highly graphic and might seem 18+ to regular people but they are essential educational material for us", "education"],
    ["instead of just watching the cricket world cup i decided to do a full data analytics project using python to predict player performance based on historical match data", "technology"],
    ["the biomechanics of a tennis serve are fascinating if you look at the physics of the kinetic chain and muscle activation required to hit the ball at that speed", "education"],
    ["business case study on how football clubs like real madrid and manchester united generate massive revenue through sponsorships and live broadcasting rights", "business"],
    ["the cloud infrastructure required to stream high definition movies to millions of concurrent users on netflix without buffering is a masterpiece of software engineering", "technology"],
    ["if you want to learn how to edit a movie trailer you should take this online course that teaches adobe premiere pro and advanced color grading techniques", "education"],
    ["the financial impact of the hollywood writers strike on the overall entertainment business and local economies is huge when you look at the lost tax revenue", "business"],
    ["for the upsc civil services exam you have to memorize the entire history of the indian constitution and understand how government policies impact the national economy", "education"],
    ["how the new government tax policy and gst registration rules are going to severely impact small business owners and online tech startups", "business"],
    ["the cybersecurity architecture protecting the electronic voting machines during the national political elections is highly sophisticated to prevent hacking and fraud", "technology"],
    ["i literally spent the entire weekend binge watching that new reality tv show and eating junk food instead of being productive and studying for my exams", "entertainment"],
    ["the referee completely ruined that football match with that terrible penalty call in the last minute of the game it was completely rigged", "sports"],
    ["these politicians are all the same just making empty promises to get votes during the election season but they never actually fix the infrastructure", "politics"],
    ["learning how to build a text classification model using tensorflow lite so i can automatically block nsfw adult content from showing up on my android phone", "technology"],
    ["i was doing research on breast cancer awareness for my neet exam and the amount of spam online is crazy but the medical textbook is super helpful", "education"],
    ["how to set up parental controls on a smartphone to block adult content and keep teenagers safe from inappropriate stuff online while they study", "safe"],
    ["i want to build a react native mobile app that fetches live movie data from a public api but im struggling with the async javascript functions", "technology"]
]

# 6. EXTREME AMBIGUITY (The "Dumb Bouncer" Bypass)
ambiguous_conversations = [
    ["the sociological impact of prostitution and brothels on public health and urbanization in developing countries", "education"],
    ["how to configure an enterprise firewall to block illegal pornography and secure corporate networks", "technology"],
    ["understanding the chemical composition of illegal street drugs and their impact on the human nervous system for medical students", "education"],
    ["documentary exploring the history of the adult film industry and its impact on copyright law and internet technology", "education"],
    ["the psychological study of addiction focusing on how easily accessible adult content alters dopamine receptors in the brain", "education"]
]

# 🔥 7. NEW: SHORT PHRASES & SEARCH QUERIES (1-3 words)
# This teaches the AI not to panic and hallucinate when users type short names or technical concepts in Chrome!
short_phrases = [
    # Safe Tech/Business Names
    ["elon musk", "technology"],
    ["sam altman", "technology"],
    ["mark zuckerberg", "technology"],
    ["sundar pichai", "technology"],
    ["steve jobs", "technology"],
    ["bill gates", "technology"],
    ["ratan tata", "business"],
    ["mukesh ambani", "business"],
    
    # Safe Engineering/Science
    ["heat transfer", "education"],
    ["fluid dynamics", "education"],
    ["thermodynamics", "education"],
    ["calculus", "education"],
    ["quantum mechanics", "education"],
    ["organic chemistry", "education"],
    ["civil engineering", "education"],
    
    # True Distractions (Entertainment/NSFW/Sports)
    ["brad pitt", "entertainment"],
    ["scarlett johansson", "entertainment"],
    ["tripti dimri", "entertainment"],
    ["tom cruise", "entertainment"],
    ["leonardo dicaprio", "entertainment"],
    ["movie trailer", "entertainment"],
    ["actress hot", "nsfw"],
    ["hot photos", "nsfw"],
    ["leaked pics", "nsfw"],
    ["bikini shoot", "nsfw"],
    ["ind vs aus", "sports"],
    ["cricket score", "sports"],
    ["football highlights", "sports"],
    ["ipl live", "sports"]
]

# 8. BORING DATA: Teach the AI what normal, safe English looks like!
boring_data = [
    ["how can i subscribe to this channel", "safe"],
    ["bro guv me the answer", "safe"],
    ["bro give as od", "safe"],
    ["can you make the latex formation for this math equation", "education"],
    ["i am not able to click this button it is broken", "technology"],
    ["what is the hot weather forecast for chennai today", "safe"],
    ["this site cant be reached err connection refused", "technology"],
    ["hey what are you doing tonight", "safe"],
    ["can you pick up milk from the grocery store", "safe"],
    ["my internet is not working please help me fix the router", "technology"],
    ["how to write a latex document for my physics homework", "education"],
    ["the temperature is so hot today i need the ac on", "safe"],
    ["please click the link below to verify your email address", "safe"],
    ["i am having trouble logging into my account", "safe"],
    ["can someone tell me the weather prediction for tomorrow", "safe"]
]

# 9. MESSY WEB DATA: Teach the AI not to panic when it reads unstructured screen dumps!
messy_web_data = [
    # Google Search Results Dump
    ["hot weather - Google Search Sign in Main menu hot weather AI Mode All Images News Videos Shopping Forums Search Results Chennai Tamil Nadu Use precise location Weather Now 34 C Cloudy Feels like 40 C Excessive heat Precipitation 10 Wind 19 kph Humidity 51 Air quality 49 Good air quality", "safe"],
    ["how to solve quadratic equations - Google Search Sign in Main menu AI Mode All Images Videos Shopping Forums Web Books Maps Flights Finance Search tools Feedback Search Results YouTube Math Tutor 10 mins ago", "education"],
    
    # Wikipedia Dump (Menus mixed with content)
    ["Wikipedia The Free Encyclopedia Main menu Search Create account Log in Personal tools Contents hide Introduction History Geography Climate Demographics Economy Transport Education Culture See also References External links Article Talk Read Edit View history Tools", "education"],
    ["Albert Einstein Wikipedia Article Talk Language Download PDF Watch Edit This article is about the physicist. For other uses see Albert Einstein disambiguation Albert Einstein was a theoretical physicist widely held to be one of the greatest and most influential scientists of all time", "education"],
    
    # YouTube Error Dump
    ["www.youtube.com This site can’t be reached www.youtube.com refused to connect. Try: Checking the connection ERR_CONNECTION_REFUSED Reload Details youtube.com/watch?v=v_JSfIPX4gs", "technology"],
    ["No internet connection You are offline Check your router or network cables Try resetting the modem ERR_INTERNET_DISCONNECTED", "technology"],
    
    # News Article mixed with Ads
    ["Read full article Subscribe now Advertisement Buy one get one free Mahindra cars latest models click here to explore The quick brown fox jumps over the lazy dog in this educational essay about wildlife conservation Share this article on Facebook Twitter", "safe"],
    ["Top stories Sign in to customise The Times of India World's hottest cities India breaks temperature records Subscribe for 1 dollar a month Advertisement click here to buy shoes online Weather patterns are shifting globally", "safe"]
]

# 10. BROKEN ENGLISH & TYPOS: Teach the AI to handle bad grammar and misspellings
broken_english_data = [
    ["how fix my compute screen not work", "technology"],
    ["pls open you tube video for crcket matc", "sports"],
    ["what is weathr tomorow in city", "safe"],
    ["downlod free movi holiwood fast", "entertainment"],
    ["hot gril photo without cloth", "nsfw"],
    ["i want mak busines start up no money", "business"],
    ["govment minster say bad word in spech", "politics"],
    ["help neet xam prep books pdf", "education"],
    ["dont kno why internet disconect", "technology"],
    ["u send me pic pls thx", "safe"],
    ["wat time is it nw", "safe"],
    ["i cant logn my acont help", "safe"],
    ["srch nearst coffe shop me", "safe"],
    ["whr is the grocry stor open", "safe"],
    ["how to cod pthon basc gam", "technology"]
]

tricky_data.extend(long_conversations)
tricky_data.extend(ambiguous_conversations)
tricky_data.extend(short_phrases)
tricky_data.extend(boring_data)
tricky_data.extend(messy_web_data)
tricky_data.extend(broken_english_data)

# Convert our new tricky data into a DataFrame
tricky_df = pd.DataFrame(tricky_data, columns=["text", "label"])

# Combine the old data with the new tricky data
combined_df = pd.concat([df, tricky_df], ignore_index=True)

# Shuffle the rows so the AI doesn't just memorize the end of the file
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save it back out
combined_df.to_csv("training_data_upgraded.csv", index=False)

print(f"✅ Successfully added {len(tricky_df)} tricky contextual sentences, short phrases, boring data, and messy web data!")
print(f"✅ Total dataset size is now {len(combined_df)} rows.")
print("✅ Saved as 'training_data_upgraded.csv'")
print(f"✅ Injected {len(boring_data) + len(messy_web_data) + len(broken_english_data)} 'Boring, Messy & Broken' grammar structures into the AI!")
print("Next step: Rename this file to 'training_data.csv' and re-run train_transformer_tf.py to update your model.tflite!")