from Bio import SeqIO
import os

def calculate_gc_content(sequence):

    sequence = sequence.upper()  # Преобразует в верхний регистр
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence)

def process_genbank_file(filename):

    sequences_with_gc = []
    for record in SeqIO.parse(filename, "genbank"):
        gc_content = calculate_gc_content(record.seq)
        sequences_with_gc.append((record.id, record.description, gc_content, str(record.seq)))

    # Сортируем последовательности по GC-составу (возрастание)
    sorted_sequences = sorted(sequences_with_gc, key=lambda x: x[2])

    for record_id, description, gc_content, seq in sorted_sequences:
        print(f"{record_id}: {description}, GC = {gc_content}")

file_path = r"C:\Users\user\PyCharmMiscProject\sequence (1).gb"
process_genbank_file(file_path)

##
from Bio import SeqIO
from Bio.Seq import Seq


def translate_cds(record):
    translations = []
    for feature in record.features:
        if feature.type == "CDS":
            try:
                # Извлечение последовательности CDS с учетом экзонов
                cds_seq = ""
                for part in feature.location.parts:
                    sub_seq = part.extract(record.seq)
                    if part.strand == -1:
                        sub_seq = sub_seq.reverse_complement()
                    cds_seq += str(sub_seq)

                # Учет рамки считывания (codon_start)
                codon_start = int(feature.qualifiers.get("codon_start", [1])[0]) - 1
                cds_seq = cds_seq[codon_start:]

                # Трансляция
                transl_table = int(feature.qualifiers.get("transl_table", [1])[0])
                protein_seq = Seq(cds_seq).translate(table=transl_table, to_stop=True)

                # Форматирование местоположения
                location = f"[{feature.location.start}:{feature.location.end}] ({'+' if feature.strand == 1 else '-'})"
                translations.append((location, str(protein_seq)))
            except Exception as e:
                print(f"Ошибка в записи {record.id}: {e}")
    return translations


file_path = r"C:\Users\user\PyCharmMiscProject\sequence (1).gb"
# Чтение файла и вывод результатов
for record in SeqIO.parse(file_path, "genbank"):
    print(f"\n{record.id}: {record.description}")
    translations = translate_cds(record)
    for loc, prot in translations:
        print(f"Coding sequence location = {loc}")
        print("Translation =")
        print(prot)
        print("-" * 50)