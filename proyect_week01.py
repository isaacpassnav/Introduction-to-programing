"""
Author: Isaac Pasapera
Create a funny tex or crazy do you use the following:

adjetive: Tired
animal: duck
verb: cruised
exclamation: of no!
verb: talk
verb: jump

"""
def grammar_correction(text):
    correction = {
        "a an": "an",
        "an a": "a",
        "is are": "are",
        "are is": "is",
    }
    words = text.split()
    corrected_word = []
    for i in range(len(words) - 1):
        pair = words[i] + " " + words[i + 1] 
        if pair in correction:
            corrected_word.append(correction[pair])
        else:
            corrected_word.append(words[i])
    corrected_word.append(words [-1])
    return " ".join(corrected_word)


print ("Complete the following asks")
adjetive = input (" Enter the adjetive: ")
animal = input( "Enter the name of animal: ")
verb = input(" Enter the verb: ")
exclamation = input(" Enter the exclamation: ")
verb1 = input(" Enter yhe verb: ")
verb2 = input(" Enter the verb: ")

print ("Proyect - cleave stories ")
print()
print(" The other day, I was really in trouble. it all started when i saw a very")
print(grammar_correction(adjetive), grammar_correction(animal), grammar_correction(verb), "down the hallway.", grammar_correction(exclamation) + "!", "i yelled. but all")
print(" i could think to do was to", grammar_correction(verb1), "over and over. miraculously,")
print(" that caused it to stop, but not before it tried to", grammar_correction(verb2))
print(" right in front of my family. ")
