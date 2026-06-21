# Sprechtext – Kombinatorik & Wahrscheinlichkeit

## Folie 1 – Titelfolie (Alle)

**Max:** Hallo zusammen! Wir sind Max, Simon und Daniel, und wir nehmen euch heute mit in die Welt
der Kombinatorik und Wahrscheinlichkeit.

**Simon:** Es geht im Grunde um eine Frage: Wie viele Möglichkeiten gibt es eigentlich wirklich –
und warum ist das fast immer viel mehr, als man im ersten Moment denkt?

**Daniel:** Wird nicht nur Theorie, es gibt auch einen Teil, wo ihr selbst mitraten müsst. Legen
wir los.

## Folie 2 – Agenda & Einstiegsfragen (Max Manahl)

Kurz zur Agenda, damit ihr wisst, was kommt: Wir starten beim Zählprinzip, das ist quasi die Basis
für alles Weitere. Danach geht's um Permutation, Variation und Kombination, dann verbinden wir das
mit dem Pascal'schen Dreieck und der Laplace-Wahrscheinlichkeit. Und ganz am Schluss gibt's einen
praktischen Teil, bei dem ihr wirklich mitmachen müsst.

Aber bevor wir starten, will ich euch noch drei Fragen stellen. Müsst nichts sagen, einfach kurz im
Kopf schätzen und euch die Zahl merken.

Wie viele verschiedene 4-stellige PIN-Codes gibt's überhaupt? Dann: Stellt euch vor, ihr alle hier
in der Klasse tauscht gegenseitig eure Handynummern aus, jeder mit jedem einmal. Wie viele
Austausche sind das am Ende insgesamt? Und die letzte: Wie wahrscheinlich ist eigentlich ein
Sechser beim Lotto 6 aus 45?

Merkt euch eure drei Schätzungen, wir lösen die nach und nach im Laufe der Präsentation auf. Simon
erklärt jetzt das Zählprinzip.

## Folie 3 – Das Zählprinzip (Simon Schick)

Das Zählprinzip ist die Grundlage für so gut wie alles, was heute noch kommt, und die Idee dahinter
ist eigentlich ziemlich simpel: Besteht etwas aus mehreren Schritten, und gibt's für jeden Schritt
mehrere Möglichkeiten, multipliziert man einfach die Möglichkeiten pro Schritt.

Nehmen wir was ganz Alltägliches: sich Anziehen am Morgen. Sagen wir, ich hab 3 Hemden, 4 Hosen und
2 Paar Schuhe zur Auswahl – wie viele komplette Outfits kann ich mir daraus zusammenstellen?

Man könnte das jetzt alles einzeln aufzählen, aber es geht einfacher: 3 Hemden mal 4 Hosen, das sind
schon mal 12 Hemd-Hosen-Kombinationen – seht ihr auch im Raster da rechts. Und jede davon kann ich
noch mit 2 Schuhen kombinieren. Macht 3 mal 4 mal 2, also 24 Outfits.

Und das Wichtige dabei: Permutation, Variation und Kombination, die gleich kommen, sind im Grunde
nichts anderes als spezielle Fälle von genau diesem Prinzip hier. Daniel zeigt euch jetzt die
Permutation.

## Folie 4 – Permutation (Daniel Kornfeld)

Bei der Permutation bringen wir alle Elemente in eine Reihenfolge – jede Position zählt dabei.

Schauen wir uns zuerst die Variante ohne Wiederholung an, an 3 Freunden – A, B und C –, die sich
nebeneinandersetzen. Im Baumdiagramm seht ihr's: für den ersten Platz gibt's 3 Möglichkeiten, für
den zweiten nur noch 2, und für den letzten bleibt eh nur noch einer übrig. 3 mal 2 mal 1, also
3 Fakultät, gleich 6 Sitzordnungen. Ganz allgemein: P(n) gleich n Fakultät. Bei 5 Leuten am Tisch
wären das schon 120 – das wächst echt schnell, dazu kommen wir später noch.

Jetzt die Variante mit Wiederholung: Wenn manche Elemente mehrfach vorkommen, müssen wir durch deren
Fakultäten teilen, sonst zählen wir Reihenfolgen doppelt, die eigentlich gleich aussehen.

Bestes Beispiel dafür ist ANANAS. 6 Buchstaben, aber das A kommt 3 mal vor und das N 2 mal. Würden
wir einfach 6 Fakultät rechnen, hätten wir viel zu viel gezählt, weil es ja optisch keinen
Unterschied macht, wenn man die drei A's untereinander vertauscht. Deshalb teilt man 6 Fakultät
durch 3 Fakultät mal 2 Fakultät mal 1 Fakultät – kommt man auf 60 Anordnungen. Max macht jetzt mit
der Variation weiter.

## Folie 5 – Variation (Max Manahl)

Bei der Variation wählen wir nur einen Teil aus – k von n Elementen –, aber die Reihenfolge spielt
eine Rolle.

Ohne Wiederholung heißt, kein Element darf doppelt gewählt werden, wie beim Ziehen ohne Zurücklegen.
Stellt euch einen Wettlauf mit 8 Läuferinnen und Läufern vor, aber nur die Plätze 1 bis 3 zählen
fürs Stockerl. Reihenfolge ist hier extrem wichtig, Gold ist nicht Silber. Für Platz 1 gibt's
8 Möglichkeiten, für Platz 2 noch 7, für Platz 3 noch 6 – macht 8 mal 7 mal 6, also 336 mögliche
Stockerl-Besetzungen, aus nur 8 Leuten.

Mit Wiederholung darf jede Stelle wieder aus allen n Möglichkeiten gewählt werden, ganz unabhängig
davon, was vorher schon dran war.

Und damit können wir die allererste Frage von vorhin auflösen: 4-stellige PIN-Codes. Jede der
4 Stellen kann eine Ziffer von 0 bis 9 sein, und Wiederholung ist erlaubt – 1-1-1-1 geht ja auch.
Also 10 hoch 4, macht genau 10.000 mögliche PINs. Schaut mal, wie nah ihr mit eurer Schätzung dran
wart. Simon erklärt jetzt die Kombination.

## Folie 6 – Kombination (Simon Schick)

Bei der Kombination ist die Reihenfolge – anders als bei Variation und Permutation – komplett egal.
Uns interessiert nur, welche Elemente überhaupt gewählt wurden, nicht in welcher Reihenfolge.

Damit lösen wir gleich unsere zweite Frage von vorhin auf: Ihr seid 15 Leute in dieser Klasse, und
jeder tauscht mit jedem die Handynummer. Wie viele Austausche sind das? Wichtig: Wenn ich mit dir
tausche, ist das dasselbe, als würdest du mit mir tauschen – die Reihenfolge ist egal, darum ist das
eine Kombination und keine Variation. Wir wählen 2 aus 15 aus, ohne dass die Reihenfolge zählt:
15 über 2, also 15 Fakultät durch 2 Fakultät mal 13 Fakultät – und das macht genau 105.

105! Die meisten schätzen da viel zu niedrig, irgendwo bei 15 oder 30. Aber weil wirklich jeder mit
jedem tauscht, wächst das viel schneller, als man im ersten Moment denkt.

Kurz noch die Variante mit Wiederholung, am Beispiel Eisbecher: Wir wählen 3 Kugeln aus 5 Sorten, und
es dürfen auch mehrere Kugeln derselben Sorte dabei sein, zum Beispiel 3 mal Schoko. Mit der Formel
kommt man da auf 35 mögliche Eisbecher. Daniel zeigt euch jetzt das Pascal'sche Dreieck.

## Folie 7 – Pascal'sches Dreieck (Daniel Kornfeld)

Das Pascal'sche Dreieck ist im Grunde eine fertige Tabelle für alle Binomialkoeffizienten – also
für all die 'n über k'-Werte, die wir bei der Kombination gebraucht haben.

Aufgebaut ist es nach einer ganz einfachen Regel: Jede Zahl ist die Summe der beiden Zahlen direkt
darüber. n über k ist also n-minus-1 über k-minus-1 plus n-minus-1 über k.

Schaut euch mal die orange 15 im Dreieck an – das ist genau 6 über 2. Kommt euch das bekannt vor?
Genau das hatten wir vorhin schon beim Lotto-Beispiel. Das Dreieck ist also keine reine Spielerei,
sondern richtig praktisch, wenn man schnell einen Binomialkoeffizienten braucht, ohne den
Taschenrechner rauszuholen. Max erklärt jetzt die Laplace-Wahrscheinlichkeit.

## Folie 8 – Laplace-Wahrscheinlichkeit (Max Manahl)

Bis jetzt haben wir nur gezählt – jetzt machen wir daraus Wahrscheinlichkeit. Die Laplace-Formel ist
eigentlich ziemlich simpel: P von A gleich Betrag A durch Betrag Omega.

Betrag A sind die günstigen Fälle, also die Ergebnisse, die unser Ereignis A erfüllen. Betrag Omega
ist einfach alles, was überhaupt passieren kann, der ganze Ergebnisraum.

Wichtig dabei: Das funktioniert nur, wenn alle Ergebnisse gleich wahrscheinlich sind – das nennt man
ein Laplace-Experiment. Bei einem fairen Würfel passt das, bei einem gezinkten nicht mehr.

Schauen wir uns das beim Würfeln an: Wir werfen zwei Würfel, wie wahrscheinlich ist ein Pasch, also
beide zeigen die gleiche Zahl? Mit dem Zählprinzip von ganz am Anfang wissen wir schon: 6 mal 6, also
36 mögliche Ergebnisse, das ist unser Omega. Und die Diagonale im Raster, das sind die 6 Fälle, wo
beide gleich sind – unser A. Also P von Pasch gleich 6 durch 36, gleich 1 durch 6.

Man sieht schön: Ohne richtig zu zählen, kommt man bei der Wahrscheinlichkeit nirgends hin. Simon
zeigt euch jetzt, was das fürs Lotto bedeutet.

## Folie 9 – Lotto 6 aus 45 (Simon Schick)

Jetzt lösen wir die letzte Frage von ganz am Anfang auf: Wie wahrscheinlich ist ein Sechser beim
Lotto 6 aus 45?

Zuerst Omega, also alle möglichen Tipps. Wir wählen 6 Zahlen aus 45, Reihenfolge egal, also eine
Kombination ohne Wiederholung: 45 über 6. Kommt da eine wahnsinnige Zahl raus – 8.145.060 mögliche
Tipps.

Und A, die günstigen Fälle? Genau 1 – nur der eine Tipp, der wirklich gezogen wird. Damit ist P von
6 Richtige gleich 1 durch 8.145.060, also ungefähr 0,0000123 Prozent.

Damit ihr ein Gefühl dafür kriegt: Das ist ungefähr so wahrscheinlich, wie wenn man unter allen
9 Millionen Leuten in Österreich zufällig genau eine bestimmte Person herauspickt. Damit sind alle
drei Fragen von vorhin geklärt – Zeit für den praktischen Teil, den übernimmt jetzt Daniel.

## Folie 10 – Praktischer Teil: Estimation-Spiel (Daniel Kornfeld)

Jetzt seid ihr dran. Wir spielen ein kleines Schätzspiel, zwei Runden.

So geht's: Wir stellen euch eine überraschende Frage, jeder schätzt für sich, im Kopf oder auf einem
Zettel – bitte kein Taschenrechner, kein Absprechen mit dem Sitznachbarn. Dann rechnen wir gemeinsam
aus, was wirklich rauskommt, und ihr seht, wie nah ihr dran wart.

Bereit für Runde 1?

## Folie 11 – Runde 1: Eure Schätzung (Max Manahl)

Hier die erste Frage: Stellt euch vor, ihr verlasst alle nacheinander das Klassenzimmer, einer nach
dem anderen. Wie viele verschiedene Reihenfolgen gibt es da – für euch 15 Schüler:innen?

Schreibt's auf oder merkt's euch gut, wir vergleichen gleich. Simon löst auf.

## Folie 12 – Runde 1: Auflösung (Simon Schick)

Das ist genau die Permutation von 15 Personen, P(15) gleich 15 Fakultät. Und 15 Fakultät ist
1.307.674.368.000. Über 1,3 Billionen.

Damit ihr ein Gefühl dafür kriegt: Stellt euch vor, ihr probiert ab jetzt eine Reihenfolge pro
Sekunde durch, ohne Pause. Wie lange würde das dauern, bis wirklich alle durch sind? Ungefähr
41.466 Jahre. Hätte man damit heute angefangen, wäre man bei ca. 39.000 vor Christus gestartet –
das ist die Steinzeit, da gab's noch nicht mal Schrift oder Landwirtschaft.

15 Fakultät heißt einfach 15 mal 14 mal 13 und so weiter bis runter auf 1 – und schon bei nur
15 Elementen kommt da diese Wahnsinnszahl raus. Daniel macht weiter mit Runde 2.

## Folie 13 – Runde 2: Eure Schätzung (Daniel Kornfeld)

Runde 2, und jetzt wird's richtig groß: Wie viele Möglichkeiten gibt's, ein Kartenspiel mit
52 Karten zu mischen?

Kleiner Tipp: Das ist eine Permutation von 52 Elementen, also P(52) gleich 52 Fakultät. Max löst
auf.

## Folie 14 – Runde 2: Auflösung (Max Manahl)

52 Fakultät ist ungefähr 8,07 mal 10 hoch 67 – eine Zahl mit 68 Stellen.

Damit ihr eine Vorstellung davon kriegt, wie groß das ist: Das sichtbare Universum hat ungefähr
10 hoch 80 Atome. 52 Fakultät ist zwar noch kleiner als das, aber stellt euch vor: Würde seit dem
Urknall jedes einzelne Atom im Universum jede Sekunde eine komplett neue Reihenfolge bilden, gäbe es
bis heute trotzdem kaum Wiederholungen.

Heißt im Endeffekt: Fast jedes Mal, wenn du Karten mischst, ist das mit ziemlicher Sicherheit eine
Reihenfolge, die es in der ganzen Menschheitsgeschichte noch nie gab – und wahrscheinlich auch nie
wieder geben wird. Simon fasst jetzt alles zusammen.

## Folie 15 – Übersichtstabelle (Simon Schick)

Bevor wir zusammenfassen, hier noch mal die kompakte Übersicht über alles, was wir heute besprochen
haben.

Der Trick, um in der Matura schnell auf die richtige Formel zu kommen, sind eigentlich nur zwei
Fragen. Erstens: Ist die Reihenfolge wichtig? Wenn ja, sind wir bei Variation, oder bei Permutation,
wenn alle Elemente verwendet werden. Wenn die Reihenfolge egal ist, sind wir bei Kombination.

Und zweitens: Wird mit oder ohne Wiederholung gewählt, also mit oder ohne Zurücklegen? Das
entscheidet dann, welche der beiden Formeln man genau nimmt.

Mit diesen zwei Fragen kommt man bei jeder Kombinatorik-Aufgabe in der Matura zur richtigen Formel.

## Folie 16 – Zusammenfassung (Alle)

**Max:** Mein wichtigster Punkt für heute: Das Zählprinzip ist die Basis von allem. Bei
unabhängigen Schritten einfach die Möglichkeiten pro Schritt multiplizieren – der Rest folgt
eigentlich daraus.

**Simon:** Für mich: Zwei Fragen bringen euch zur richtigen Formel. Ist die Reihenfolge wichtig?
Und wird mit Wiederholung gewählt? Wenn ihr die zwei Fragen stellt, findet ihr in der Matura immer
die passende Formel.

**Daniel:** Und von mir: Mit Laplace, P von A gleich Betrag A durch Betrag Omega, werden aus
abstrakten Kombinatorik-Formeln plötzlich ganz konkrete Wahrscheinlichkeiten – beim Würfeln, beim
Lotto, oder beim Kartenmischen.

## Folie 17 – Quellen (Alle)

**Max:** Hier noch kurz unsere Quellen: Lehrplan und Formelsammlung vom BMBWF, unser Schulbuch,
mathe-online.at, die Österreichischen Lotterien für die Lotto-Zahlen, und Wikipedia für die
Begriffe. Alle Grafiken haben wir selbst mit Python erstellt.

## Folie 18 – Danke / Fragen (Alle)

**Max:** Damit wären wir fertig.

**Simon:** Danke für eure Aufmerksamkeit!

**Daniel:** Habt ihr noch Fragen? Oder sagt uns – was war eure überraschendste Zahl heute?
