# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The new game button does not work, it should get rid of the textbox that tells you to click the new game button and should let you be able to enter in guesses just like how it did in the first game. The hints are misleading, tells you to go lower if the secret is larger and vice versa. The differences between modes are a bit confusing as well. All modes you have to guess the number between 1 and 100 and attempts for normal is 8 while easy which probably should allow more attempts instead allows fewer attempts than normal. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I used Claude's chat as well as Copilot's inline feature as well. 

  When Claude suggested edits, it made a misleading edit in which the range of the secret was the same for all, I thought this was misleading since I feel easy, normal, and hard should all have different ranges. I was able to verify by understanding the code, and fixing it for myself. 

  One AI suggestion that was correct was describing the logic and finding where that was misleading where the original code was calculating the score. I was able to verify by reading through the code myself. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  By doing the pytests as well as looking at the actual game and trying it out in different ways. One test was to see whether the hints made sense. This was done both manually and with pytest, it showed that the hints were confusing but after fixing it, it showed what the user would see and that it made sense for the user. AI helped design the pytests for me, and that helped me because I was able to create many tests and see if the code fixes actually worked before verifying it myself manually. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would say that reruns are like starting a new game in a guessing game, but with a new secret that you have to guess so that you can play an infinite amount of times. Session state helps so that when you are guessing, the secret stays the same each time. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  I think I would use AI to understand my code better, and actually try to do the fixes like asking AI to explain the code but not try to fix it. I also really liked the commit message feature which I didn't know to use before, it was very helpful as I often struggle to condense my changes into one sentence or short amount of words. 
