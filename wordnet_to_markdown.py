import os
from nltk.corpus import wordnet as wn

output_directory = "wordnet_markdown"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

synsets = list(wn.all_synsets())

for synset in synsets:
    sanitized_name = synset.name().replace("/", "_")
    simple_name = sanitized_name.split(".")[0]
    filename = f"{output_directory}/{simple_name}.md"

    # Prüfen, ob die Datei bereits existiert, und erstellen Sie sie, wenn sie nicht vorhanden ist
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("")

    with open(filename, "a", encoding="utf-8") as f:
        # Schreiben Sie die Überschrift (Synset-ID und Wortart)
        f.write(f"# {sanitized_name} ({synset.pos()})\n\n")

        # Schreiben Sie die Definition
        f.write(f"**Definition:** {synset.definition()}\n\n")

        # Schreiben Sie die Beispiele (falls vorhanden)
        if synset.examples():
            f.write("**Examples:**\n\n")
            for example in synset.examples():
                f.write(f"- {example}\n")
            f.write("\n")

        # Schreiben Sie die Synonyme (Lemmata)
        f.write("**Synonyms:**\n\n")
        for lemma in synset.lemmas():
            f.write(f"- {lemma.name()}\n")
        f.write("\n")

        # Schreiben Sie die Hypernym-Beziehungen (Oberbegriffe)
        hypernyms = synset.hypernyms()
        if hypernyms:
            f.write("**Hypernyms:**\n\n")
            for hypernym in hypernyms:
                sanitized_hypernym_name = hypernym.name().replace("/", "_")
                simple_hypernym_name = sanitized_hypernym_name.split(".")[0]
                f.write(f"- [[{simple_hypernym_name}]]\n")
            f.write("\n")

        # Schreiben Sie die Hyponym-Beziehungen (Unterbegriffe)
        hyponyms = synset.hyponyms()
        if hyponyms:
            f.write("**Hyponyms:**\n\n")
            for hyponym in hyponyms:
                sanitized_hyponym_name = hyponym.name().replace("/", "_")
                simple_hyponym_name = sanitized_hyponym_name.split(".")[0]
                f.write(f"- [[{simple_hyponym_name}]]\n")
            f.write("\n")

        # Fügen Sie eine Trennlinie hinzu, um die verschiedenen Bedeutungen voneinander zu trennen
        f.write("---\n\n")
