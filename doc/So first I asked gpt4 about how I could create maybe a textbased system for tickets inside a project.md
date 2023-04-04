# That's the story how I discussed a versioncontrollable text-based ticket system

[ Cutmasta-Kun ]

Hallo. Ich würde gerne in einem Projekt eine Art "Ticketsystem" integrieren, bei dem ich durch versionskontrolle (in dem Fall Git) den status meiner arbeit verfolgen kann.
Dafür müsste es Textbasiert sein und relativ leicht verständlich und übersichtlich sein. Ich denke Markdown könnte dabei ebenfalls helfen.
Hast du vielleicht eine Idee?

[ Helper-Chan ]

Hallo! Eine Möglichkeit, ein textbasiertes Ticketsystem mit Versionskontrolle über Git zu erstellen, wäre die Verwendung von Markdown-Dateien zur Verwaltung Ihrer Aufgaben. Hier ist eine einfache Struktur, die Sie verwenden können:

1. Erstellen Sie ein Repository für Ihr Projekt (falls noch nicht vorhanden) und klonen Sie es auf Ihren lokalen Computer.
2. Erstellen Sie im Hauptverzeichnis Ihres Repositorys ein Verzeichnis namens "tickets".
3. Für jedes Ticket, das Sie erstellen möchten, erstellen Sie eine neue Markdown-Datei (.md) im "tickets"-Verzeichnis. Verwenden Sie eine aussagekräftige Namenskonvention für die Dateien, z. B. Ticket-001-Implementierung-Funktionalität-X.md.
4. In jeder Markdown-Datei können Sie die Details des Tickets angeben. Hier ist ein Beispiel für eine einfache Struktur:
``` markdown
# Titel des Tickets

## Beschreibung
Eine kurze Beschreibung des Tickets und was es beinhaltet.

## Anforderungen
- [ ] Anforderung 1
- [ ] Anforderung 2
- [ ] Anforderung 3

## Status
- Erstellt: (Datum)
- Zuletzt aktualisiert: (Datum)
- Fälligkeitsdatum: (Datum, falls zutreffend)
- Verantwortlich: (Ihr Name oder der Name des zuständigen Teammitglieds)

## Kommentare
- (Datum) Kommentar 1
- (Datum) Kommentar 2
```
5. Sobald Sie ein Ticket erstellt oder aktualisiert haben, fügen Sie die Änderungen dem Git-Repository hinzu, commiten Sie sie und pushen Sie sie in das Remote-Repository.
6. Um den Status Ihrer Tickets zu verfolgen, verwenden Sie Git-Log oder Git-Blame, um die Änderungshistorie für jede Datei zu sehen.
7. Optional können Sie auch Git-Branches verwenden, um an verschiedenen Tickets parallel zu arbeiten und sie später in den Haupt-Branch zu integrieren.

Durch diese Struktur haben Sie ein einfaches, textbasiertes Ticketsystem, das vollständig in Ihr Git-Repository integriert ist. Es ist leicht verständlich, übersichtlich und bietet die Vorteile der Versionskontrolle durch Git.