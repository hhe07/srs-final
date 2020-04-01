# Existing Code
## Newdict:
- Test, with Line 30464 and 650 type scenarios.

## BabelQuery:
- Fix the findCommon methods, ask Edward or Torrence for help making it less exponential.
- Remove Japanese/Non-Simplified/English words from Related output. (done, test)

## Markov:
- Calculate Probabilities based on occurance counts now that they actually exist! (Done)
- Perhaps add a "total" key to the dictionary to record stuff? (Done)
- Add option to dump all the outputs! (Done)
- Efficiency!
- Test

# New Code
## Word Translation System
- All lowercase!
- Use (first) Newdict and search for the correct word.(done)
- If not, go to BabelQuery.(done)
- Perhaps add option for "precision" mode that uses both? (done)
- Done, rerun newdict to reflect the new lowercase, or remove lowercase meme?
- See if can add BabelQuery module that returns highest matched term instead of all.

## Classifier Contextualiser
- Should read from existing text.
- Given a series of nouns relating to a classifier:
- BabelQuery them and get some related ideas.
- Identify surrounding grammar?
- Store information!!!

## Conjoiner Contextualiser
- Similar idea
- Read from existing text
- If conjoiner, then record before/after term types
- Store information!!!

# Further Down The Line
- Markov Model Merge Probabilities? (E-C * C)
- Download and tag corpora
- Train sentence Markov models
- Phrase detection? (requires further thought)
- Run the contextualisers and get information
- Start work on putting it all together.
- After putting it all together, test against Google Translate - get the API?

# 07/01/20: Main Translation Script
- Start
- Expects text file to translate
- Expects sentence Markov model pickles.
- Expects classifier/conjoiner models.
- Expects valid API key
- for each sentence:
  - create translatedSentence datatype
  - tag POS
  - Predict Chinese POS sequence by generating based on probabilities: E-C * C or some other approach to using both E-C and C
    - Generate and then confirm: if greater than 50% probability or something then it's fine?
  - Go through, for each POS:
    - if normal, send through translation pipeline, add into sentence
      - Translation Pipeline: Dictionary (manipulated, good methods to get information), then BabelNet (Get related words, ideally with probabilities)
        - BabelNet: Requires getSenses, getEdges methods to really do anything.
    - if conjoiner position, select proper based on models, run through decision model.
    - if classifier position, select proper based on models, run through decision model.
  - Return translatedSentence
- Repeat until finished, output to text file.

# 07/01/20: New Set of ToDos:
- Finish proposal and paperwork (proposal finished, contact Torrence about paperwork 08/01/19)
- Test and fix existing modules/code (~1 hr) (Done!)
- Figure out Google Translate API Access (~1 hr)
- See if BLEU/METEOR work (~1 hr)
- Term datatype? With automated flow outlined in 'for each POS'? There was one datatype I was thinking of earlier that I should implement (~30 min, excluding testing)
- POS Model Builder: Using the Markov system I have, scan through a text file, tag POS, and train the models! (~40 min)
  - Confirm by creating a sample sequence based on the probabilities (~10 min)
- For sure want a 'generate' system for Markov system (~30 min)
- Classifier Model Builder: Using the Markov system, scan through a series of pairs of classifiers and their surroundings, build a relationship of what BN information is related to the classifier (~2 hrs)
- Finish getRelated of babelQuery (~40 min) (DONE! IT WORKS!)
- See if babelQuery can return highest prob matched (~30 min)
- Rerun newdict to reflect lowercase only (~10 min) (DONE!)
- Conjoiner Model Builder: Given the context, generate some sort of data. (~1 hr)
- Build Main Translation Script (~2 hr)
- Build Corpora processing script: divide into chunks for POS model builder, or build processing into each of the model builders. (~2 hr)
- Change getEdges to return a list so everything is far easier.

Useful:
- Map: Apply function to all
- Filter: Returns all that return True

08/01/19: What do I have so far?
- Semi-Functional but untested newdict
  - Definition class with working parser
  - Dictionary that creates Definitions and splits (in theory)
  - Retrieve method
- Fully functional BabelQuery
- Fully functional getRelated (albeit without some features)
- Non-Functional getEdges
- Semi-Functional Markov Model system.
- untested, likely semi-functional translation pipeline

08/01/19: Testing each of the semi-functional things
- newdict (IT WORKS! \o/)
  - Rerun with lowercase
  - Also, try looking for match for ALL original terms - if no match found then that's no good
  - newdict checkfiles and retrieve is broken!!!
  - Fix the "div" statement - it's broken!
- getEdges (IT WORKS!)
  - When done, find some similar terms (corn, rice) and see if it does what it intends.
  - The whole idea of the final thing is to first see if a correlation can be found within reasonable distance, otherwise just dump the original and all of its related, might require further thought
- Markov Model System (IT WORKS! YAAAS!) 
  - Try training a test based on a basic, fairly simple test file with some states (e.g. "a","b","c")
  - Try the "generate" and see if it generates at least something.
  - CALCPROB IS BROKEN!!!
- Translation Pipeline
  - Fairly linear, just put some words through with the "accuracy" option set to yes or no.


Results
- G undercounted by 1
- ' overcounted by 1
- S undercounted by 1

if count>len(l)-1:
                break

Stuff like this will cause deep bad, use >=

This is causing some trouble: ü :(

IT WORKS!

# tmp from getedges:
```
print("pass") 
        edge1 = bq.getEdges(queue1[0],key)
        print(len(edge1))
        edge2 = bq.getEdges(queue2[0],key)
        print(len(edge2))
        for x in edge1:
            for y in edge2:
                if x["target"]==y["target"]:    
                    common.append(x["target"])
        common = list(dict.fromkeys(common))
        if len(common)>0:
            break
```
# getEdges
- Init with rid1, rid2, pos, pass count, key
- If passcount is not specified do 1 pass from initial.
- Queue1
- Queue2
- Final1
- Final2
- Queue1 initialised with rid1
- Queue2 initialised with rid2
- Get for rid1 > tmp1
- Get for rid2 > tmp2
- Queue1 = tmp1
- Queue2 = tmp2


# 21/01/20: New Set of ToDos:
2. Figure out Google Translate API Access (~1 hr)
3. See if BLEU/METEOR work (~1 hr)
5. Classifier Model Builder: Using the Markov system, scan through a series of pairs of classifiers and their surroundings, build a relationship of what BN information is related to the classifier (~2 hrs)
6. Translation pipeline
7. Build Main Translation Script (~2 hr)
8. Build Corpora processing script: divide into chunks for POS model builder, or build processing into each of the model builders. (~3 hr)
   1. Collect conjoiners
   2. Collect classifier contexts
   3. Collect POS transitions: parallel and otherwise, train models based on them.
   4. Modify Markov to have a "reset" tag in the middl that will just start transition recording again.
9. Problem: POS tags included may not be compatible with what's actually in the sentence.

## Moved
4. Term datatype? With automated flow outlined in 'for each POS'? There was one datatype I was thinking of earlier that I should implement (~30 min, excluding testing)
5. See if babelQuery can return highest prob matched (~30 min) (domains, weight, frequency all not super useable, consider in next iteration)

- Rework Dictionary for static retrieval, retrieve actual words

6. Conjoiner Model Builder: Given the context, generate some sort of data. (~1 hr)(Finished)
7. 2. Requires somewhat substantial modification of markov system (finished)
8. 1. Finish proposal and paperwork (proposal finished, contact Torrence about paperwork 08/01/19)
9. 4. POS Model Builder: Using the Markov system I have, scan through a text file, tag POS, and train the models! (~40 min)
   1. Confirm by creating a sample sequence based on the probabilities (~10 min)


02/02/20:
1. POS Creator needs some testing once some actual data is in place (~1 hr)
2. Build script to tag POS, train ZH and bilingual MM (make sure to include sentence start, "zh" in front of Chinese) (1 hr) (Monday)
3. Fix Newdict (1 hr) (Tuesday)
4. Translation Pipeline (Wednesday during after-school robotics)
5. Conjoiner MM trainer and user (1 hr) (Friday)
6. Classifier data finder (2 hr)
7. 