## Abschließende Mitteilung

#### an das Presse- und Informationsamt der Bundesregierung über die Prüfung

## Einsatz künstlicher Intelligenz zur Information der Bundesregierung

#### Teil 3 – BPAvis

Diese Prüfungsmitteilung enthält das vom Bundesrechnungshof abschließend im Sinne
des § 96 Absatz 4 Satz 1 BHO festgestellte Prüfungsergebnis. Sie ist auf der Internetseite
[des Bundesrechnungshofes veröffentlicht (www.bundesrechnungshof.de).](http://www.bundesrechnungshof.de/)


Gz.: VII 3 - 0001818/3 7. April 2025


Die Mitteilung des Bundesrechnungshofes ist urheberrechtlich geschützt.


**Inhaltsverzeichnis**


0 Zusammenfassung 5


1 Das Verfahren BPAvis 8


1.1 Kriseninfrastruktur 8


1.2 Zugriff für Bundesbehörden 8


1.3 Projektphase BPAvis 2.0 und Kosten 9


2 IT-Sicherheit 10


2.1 Sachverhalt 10


2.1.1 IT-Sicherheitskonzept 10
2.1.2 Audit Log 11


2.2 Würdigung 11


2.3 Empfehlung 12


2.4 Stellungnahme 12


2.5 Abschließende Würdigung 12


3 IT-Betrieb 12


3.1 Sachverhalt 12


3.1.1 Service Level Agreement und Notfallkonzept 13
3.1.2 Hochverfügbarkeit 13


3.2 Würdigung 13


3.3 Empfehlung 14


3.4 Stellungnahme 14


3.5 Abschließende Würdigung 15


4 Wirtschaftlichkeit 15


4.1 Sachverhalt 15


2


4.2 Würdigung 16


4.3 Empfehlung 16


4.4 Stellungnahme 17


4.5 Abschließende Würdigung 17


3


**Abkürzungsverzeichnis**


_**B**_


BPA _Presse- und Informationsamt der Bundesregierung_
BPAvis _BPA_ _Verteil-Informationssystem_
BSI _Bundesamt für Sicherheit in der Informationstechnik_


_**H**_


HANA _High-performance ANalytic Appliance_


_**I**_


IT-RK _IT-Rahmenkonzept_


_**S**_


SLA _Service Level Agreement_


_**U**_


UP Bund _Umsetzungsplan Bund 2017_


_**W**_


WiBe _Wirtschaftlichkeitsbetrachtung_
WU _Wirtschaftlichkeitsuntersuchung_


4


# 0 Zusammenfassung

Das Presse- und Informationsamt der Bundesregierung (BPA) erfüllt als Dienstleister für die
Bundesregierung, die Bürgerinnen und Bürger sowie die Medien zwei wesentliche Aufgaben:


- interne Information für politische Entscheidungsträgerinnen und Entscheidungsträger so­
wie die Beschäftigten der Bundesverwaltung und

- Information über die Arbeit der Bundesregierung nach außen.


Das BPA wertet eine Vielzahl an Quellen aus, z. B. nationale und internationale Nachrichten­

ticker, Zeitungen und soziale Medien. Die Beschäftigten des BPA nutzen dazu insbesondere
die Verfahren „ _NewsCenter_ “ und „BPA Verteil-Informationssystem“ (BPAvis). Der Bundes­
rechnungshof hat _NewsCenter_ und BPAvis sowie die dazugehörigen Projekte geprüft. Beide

Verfahren befanden sich im Oktober 2023 im Wirkbetrieb. Das BPA hatte ab dem Jahr 2018

damit begonnen, vorherige Altverfahren abzulösen und auf einer gemeinsamen Plattform zu
konsolidieren. Es plante, kritische IT-Verfahren in einem georedundanten Ausweichrechen­

zentrum am Dienstsitz Bonn zu betreiben.


Die vorliegende Abschließende Mitteilung, Teil 3 umfasst die Feststellungen zu BPAvis, z. B.
zur IT-Sicherheit und zur Wirtschaftlichkeit. Die Prüfungserkenntnisse zu _NewsCenter_ sowie
zum Aufbau eines georedundanten Ausweichrechenzentrums beschreibt der Bundesrech­
nungshof in weiteren Abschließenden Mitteilungen.


Er stellt im Wesentlichen Folgendes abschließend fest:


0.1 Mit dem IT-Verfahren BPAvis empfängt, bearbeitet, verteilt und recherchiert das BPA
Meldungen von Nachrichtenagenturen. Rund um die Uhr unterrichtet es u. a. den

Bundeskanzler, den Bundespräsidenten, die Mitglieder der Bundesregierung und alle

Ressorts. Das BPA bezeichnet BPAvis als Kriseninfrastruktur. Es sei „essentieller Be­

standteil der Krisenkommunikation“ und „Gegenstand der Krisenpläne“ der Bundesregierung. Bis Oktober 2023 gab das BPA für BPAvis 6,4 Mio. Euro aus. Um BPAvis zu

betreiben und weiterzuentwickeln, rechnet es in den Jahren 2024 bis 2027 mit weite­

ren Ausgaben von 4,4 Mio. Euro. (Tz. 1)


0.2 Das BPA hat gegen den Umsetzungsplan Bund 2017 (UP Bund) verstoßen, da es für
BPAvis als kritisches IT-Verfahren über zwei Jahre nach Überführung in den Wirkbe­
trieb über kein gültiges IT-Sicherheitskonzept verfügt.


Das BPA muss zeitnah ein IT-Sicherheitskonzept zu BPAvis vorlegen und künftig fort­
schreiben. Die Vorgaben des UP Bund hat es vollumfänglich einzuhalten.


Das BPA hat mitgeteilt, dass es das IT-Sicherheitskonzept zu BPAvis fertiggestellt
habe und künftig fortschreiben werde.


Das BPA setzt die Empfehlung des Bundesrechnungshofes bereits um. (Tz. 2)


5


0.3 In seinem Betriebshandbuch legte das BPA fest, dass BPAvis 24 Stunden an 7 Tagen in
der Woche (24/7) verfügbar sein müsse. Es strebte dabei eine Ausfallsicherheit von
mehr als 99,7 % an. Die interne Hotline von BPAvis war lediglich innerhalb der norma­

len Dienstzeiten erreichbar. Dies ist für den IT-Betrieb eines Verfahrens, das die Kri
senkommunikation der Bundesregierung sicherstellen soll, inakzeptabel. Es ist nicht
sichergestellt, dass das BPA Fehler in BPAvis zeitnah beheben kann. Für BPAvis fehlt
zudem ein Notfallkonzept, was den Wiederanlauf des Systems gefährdet hat.


Es ist zwingend erforderlich, dass das BPA die Servicezeiten der internen Hotline für
BPAvis ausweitet. Das BPA sollte für BPAvis ein eigenes Notfallkonzept erstellen.


Das BPA hat dargestellt, es prüfe,


   - die fehlenden Notfallkonzepte zu erstellen und

   - die Servicezeiten der Hotline auszuweiten.


Zu den Servicezeiten erläuterte es, es könne nicht ausgewählte Beschäftigte des La­
gezentrums fortbilden, um die Hotline zu besetzen. Aufgrund des Schichtdienstes
müsste es dann _alle_ Beschäftigten des Lagezentrums fortbilden. Dies wirke sich mög­
licherweise auf die tarifliche Eingruppierung der Beschäftigten aus. Für den Regelbe­
trieb könne das BPA dieser Empfehlung daher nicht folgen. Die hohe Verfügbarkeit
von BPAvis stelle es durch den parallelen und weitgehend unabhängigen Betrieb im
Rechenzentrum Berlin, dem Cloud-gestützten Notfallsystem sowie perspektivisch ei­
ner georedundanten Instanz von BPAvis im Rechenzentrum Bonn sicher. In einer
Krise hingegen könne es über organisatorische Regelungen längere Servicezeiten er­
möglichen.


Das BPA will der Empfehlung des Bundesrechnungshofes zu den Notfallkonzepten
folgen. Die Hinweise des BPA zur Eingruppierung seiner Beschäftigten sind nachvoll­
ziehbar. Es sollte weiter prüfen, wie es die Servicezeiten der Fachadministration auch
für den Regelbetrieb ausweiten kann. (Tz. 3)


0.4 Das BPA hat für BPAvis weder eine Wirtschaftlichkeitsbetrachtung (WiBe) in der Pla­
nungsphase erstellt noch hat es Erfolgskontrollen durchgeführt.


Das BPA hat für BPAvis zeitnah eine begleitende Erfolgskontrolle anhand konkreter,
mit messbaren Indikatoren unterlegter Ziele durchzuführen. Die Ergebnisse der Er­
folgskontrolle sollte es geeignet berücksichtigen, wenn es BPAvis weiterentwickelt.


Das BPA hat entgegnet, es habe innerhalb von sechs Wochen nach der Überführung
von BPAvis in den Wirkbetrieb eine Erfolgskontrolle durchgeführt. Es habe das dazu­
gehörige Projekt erfolgreich abgeschlossen.


6


Das BPA konnte dem Bundesrechnungshof keine Erfolgskontrollen von BPAvis vorle­
gen. Der Bundesrechnungshof hält daher an seinen Empfehlungen fest. Eine abschlie­
ßende Erfolgskontrolle durchzuführen, ist haushaltsrechtlich vorgeschrieben. (Tz. 4)


7


# 1 Das Verfahren BPAvis

Mit dem IT-Verfahren BPAvis empfängt, bearbeitet, verteilt und recherchiert das BPA Mel­
dungen von zehn [1] Nachrichtenagenturen. Es unterrichtet rund um die Uhr


- den Bundeskanzler,

- den Bundespräsidenten,

- die Mitglieder der Bundesregierung,

- das Bundestagspräsidium,

- die Regierungssprecher und

- alle Ressorts sowie das BPA.


Dazu richtete das BPA ein Lagezentrum ein. Die Beschäftigten im Lagezentrum arbeiten in
Schichten, um einen 24/7-Dienst sicherstellen zu können. Im Lagezentrum gehen ca. 1,8 Mil­
lionen Meldungen pro Jahr ein. Das BPA speichert und bearbeitet die Meldungen zunächst.
Pro Jahr verteilt es ca. 70 000 davon weiter. [2] Alle politisch relevanten Meldungen überführt
das BPA zudem per Schnittstelle in sein _NewsCenter_ .

### 1.1 Kriseninfrastruktur


Das BPA bezeichnet BPAvis in seinem IT-Rahmenkonzept (IT-RK) 2024 als „Kriseninfrastruk­
tur“ [3] . BPAvis nehme eine besondere Rolle in der Unterrichtung der Bundesregierung ein. Es
sei Gegenstand der Krisenpläne der Bundesregierung und essentieller Bestandteil der Krisen­

kommunikation.


Im Oktober 2023 betrieb das BPA BPAvis im eigenen Rechenzentrum am Dienstsitz Berlin.
Darüber hinaus hatte es ein dauerhaft verfügbares Cloud-Notfallsystem [4] eingerichtet.

### 1.2 Zugriff für Bundesbehörden


Beschäftigte der Bundesverwaltung können über die Netze des Bundes auf BPAvis zugreifen
und BPAvis kostenfrei nutzen. Dazu müssen sie sich vorher einmalig registrieren. Über die

Nutzeroberfläche können sie auswählen, ob sie


1 U. a. Agence France-Presse, dpa Deutsche Presse-Agentur GmbH, Associated Press und Reuters. Das BPA

empfängt die Meldungen teils direkt per Satellit.
2 Bei Meldungen von höchster Wichtigkeit ist dazu z. B. auch ein Versand per _Short Message Service_ direkt an

Mobiltelefone von Mitgliedern der Bundesregierung vorgesehen.
3 BPAvis ist keine Anwendung der KRITIS-Infrastruktur im Sinne der KRITIS-Rechtsverordnung oder des KRITIS
Dachgesetzes. BPAvis dient dazu, in Krisen die „Medienlage“ zu erstellen und der Bundesregierung zugäng­

lich zu machen.

4
In der _Microsoft Azure Cloud_ .


8


- in sämtlichen Meldungen oder

- bereits vom Lagezentrum ausgewählten, politisch relevanten Meldungen


recherchieren wollen. Anschließend können sie über eine interaktive Benutzeroberfläche su­

chen. Mit „Filtern“ kann die Suche weiter eingeschränkt werden, z. B. nach Ressorts, Agentu­

ren oder Datum der Meldung. Die Suchergebnisse können Nutzerinnen und Nutzer anschlie­
ßend ablegen, exportieren, drucken oder per E-Mail versenden.


Wir werteten aus, welche Behörden und Einrichtungen Zugänge für BPAvis angelegt hatten
(Abbildung 1). Das BPA hatte über 700 Zugänge für seine Beschäftigten eingerichtet. Auch

das Bundeskanzleramt und alle Bundesministerien hatten Zugänge eingerichtet. Drei Bun­
desministerien kamen auf eine dreistellige Anzahl an Zugängen. Bei den meisten Bundesmi­
nisterien beschränkte sich der Zugriff auf Pressestellen und Lagezentren sowie die Büros der
Mitglieder der Bundesregierung und der politischen Beamtinnen und Beamten.


Abbildung 1
### Zugänge zu BPAvis

Hauptnutzer von BPAvis ist das BPA. Darüber hinaus legten einige Bundesministerien (inklu­
sive Geschäftsbereichsbehörden) eine dreistellige Anzahl an Zugängen an.


716



Grafik: Bundesrechnungshof. Quelle: Auswertung von Erhebungsdaten, Stand: 2. Oktober 2023.

### 1.3 Projektphase BPAvis 2.0 und Kosten





Im November 2018 begann das BPA mit einem „Vorprojekt“ zu BPAvis. Es bezeichnete sein
Vorhaben als „BPAvis 2.0“. Mit dem Projekt wollte es ein Altsystem [5] ablösen und verstärkt
auf Standard-Komponenten [6] des Herstellers SAP setzen. In den Jahren 2019 bis 2021 entwi­
ckelte das BPA BPAvis neu. Im August 2021 überführte es BPAvis in den Wirkbetrieb.


5 Im Zusammenhang mit dem Projekt teils als „BPAvis 1.0“ bezeichnet. Das BPA musste BPAvis 1.0 zwingend

ablösen, da es keinen stabilen Betrieb mehr gewährleisten konnte und Sicherheitslücken bestanden.
6 Beim von uns geprüften BPAvis handelt es sich um ein IT-Verfahren, das technisch auf Standardkomponen­

ten des Herstellers SAP aufbaut. Kernstück ist eine SAP HANA ( _High-performance ANalytic Appliance_ ) Da­
tenbank sowie die Datenmanagement-Software SAP _Data Intelligence_ .


9


Das BPA hatte ursprünglich geplant, den Wirkbetrieb bereits im Januar 2021 aufzunehmen.
Aufgrund der Corona-Pandemie [7] und aus weiteren betrieblichen Gründen [8] verzögerte sich
diese Zeitplanung um acht Monate.


Innerhalb des Projektes gab das BPA für BPAvis insgesamt 5,1 Mio. Euro aus. Der darauffol­
gende Wirkbetrieb bis einschließlich Oktober 2023 kostete 1,3 Mio. Euro. Für die Jahre 2024
bis 2027 plante das BPA weitere Ausgaben von 4,4 Mio. Euro (siehe Abbildung 2). Es beab­
sichtigte u. a., BPAvis in den _NewsCenter-_ Verbund zu integrieren und im Jahr 2024 neu zu

entwickeln.


Abbildung 2
### Ausgaben für BPAvis

Bis Oktober 2023 gab das BPA für das Projekt BPAvis 2.0 und den IT-Betrieb 6,4 Mio. aus. Für
die Jahre 2024 bis 2027 rechnet es mit weiteren Ausgaben von 4,4 Mio. Euro.



5,1 Mio. Euro



4,4 Mio. Euro



Projekt BPAvis 2.0 Betrieb bis Oktober 2023 SOLL 2024 bis 2027


Grafik: Bundesrechnungshof. Quelle: Auswertung von Erhebungsdaten.

# 2 IT-Sicherheit

### 2.1 Sachverhalt

#### 2.1.1 IT-Sicherheitskonzept


Der UP Bund legt als verbindliche Informationssicherheitsleitlinie des Bundes u. a. fest, wie
Bundesbehörden ihre Informationen und IT-Systeme absichern müssen. [9] Demnach sind ITSicherheitskonzepte zu kritischen Geschäftsprozessen „vorrangig zu erstellen“ [10] . Gemäß IT
RK 2024 des BPA ist BPAvis „unverzichtbar“ und Teil der „Kriseninfrastruktur“.


7 Das BPA nannte hier z. B. gesundheitsbedingte Ausfälle beim Auftragnehmer und _Home-Schooling_ bei den


Entwicklerinnen und Entwicklern.
8 Hierzu führte das BPA u. a. Stabilitätsprobleme der Software, Bauvorhaben und „hohe Abhängigkeiten“ an.
9 UP Bund, Leitlinie für die Informationssicherheit in der Bundesverwaltung, S. 3.
10 Ebenda, S. 11.


10


Im März 2021 gab das BPA in einem internen Vermerk an, das IT-Sicherheitskonzept für
BPAvis sei in Erstellung. Es beabsichtigte, dieses bis September 2021 zu erarbeiten und im
Oktober 2021 durch den Informationssicherheitsbeauftragten freigeben zu lassen. Dabei
stellte es auch fest, dass die formalen Voraussetzungen für den Go-Live erst mit der Ab­
nahme des Sicherheitskonzepts gegeben seien. Am 3. August 2021 überführte das BPA BPA­

vis in den Wirkbetrieb.


Im Jahr 2022 war das IT-Sicherheitskonzept in Arbeit. Im Januar 2023 stellte das BPA dar,


- dass es BPAvis ohne IT-Sicherheitskonzept in den Wirkbetrieb überführt habe,

- das IT-Sicherheitskonzept noch ausstehe und

- ein externer Dienstleister das IT-Sicherheitskonzept bis „Spätsommer“ 2023 fertigstellen

werde.


Im März 2024 räumte das BPA ein, dass es für BPAvis noch kein IT-Sicherheitskonzept erstellt
hatte. Es beabsichtigte, dieses im Laufe des Jahres 2024 fertigzustellen.

#### 2.1.2 Audit Log


SAP empfiehlt als sogenannte „ _Best Practice_ “, in HANA Datenbanken stets das „ _Audit Log_ “ zu
aktivieren. Dies gewährleiste, sicherheitskritische Ereignisse, z. B. Änderungen an der SAPSystemumgebung, nachvollziehen zu können. [11] Das Bundesamt für Sicherheit in der Infor­
mationstechnik (BSI) empfiehlt, die wichtigsten Sicherheitsaufzeichnungsfunktionen von
SAP-Systemen wie das _Audit Log_


- kontinuierlich zu überwachen und

- bei verdächtigen Vorfällen automatisch die zuständigen Beschäftigten zu alarmieren. [12]


Das BPA hatte das _Audit Log_ bei BPAvis deaktiviert.

### 2.2 Würdigung


Das BPA hat gegen den UP Bund verstoßen, da es für BPAvis als kritisches IT-Verfahren auch
über zwei Jahre nach Überführung in den Wirkbetrieb kein gültiges IT-Sicherheitskonzept
vorlegen kann. Wie es selbst bereits festgestellt hat, hätte es BPAvis ohne IT-Sicherheitskon­
zept nicht in den Wirkbetrieb überführen sollen.


11 ­
[Dokumentation von SAP zu HANA, z. B. https://help.sap.com/docs/SAP_HANA_PLAT](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/ddcb6ed2bb5710148183db80e4aca49b.html)

[FORM/b3ee5778bc2e4a089d3299b82ec762a7/ddcb6ed2bb5710148183db80e4aca49b.html, zuletzt aufge­](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/ddcb6ed2bb5710148183db80e4aca49b.html)

rufen am 13. Februar 2025.
12 IT-Grundschutz-Kompendium des BSI, APP.4.2.A32 (Echtzeiterfassung und Alarmierung von irregulären Vor­

gängen).


11


Das BPA hat die Nachvollziehbarkeit sicherheitskritischer Ereignisse in BPAvis gefährdet, in­
dem es das _Audit Log_ deaktiviert hat. Damit hat es sich weder an die Empfehlungen des BSI
noch an die des Herstellers gehalten.

### 2.3 Empfehlung


Das BPA muss das IT-Sicherheitskonzept zu BPAvis zeitnah fertigstellen und fortschreiben.


Das BPA sollte das _Audit Log_ wieder aktivieren, um sicherheitskritische Ereignisse in BPAvis
künftig nachvollziehen zu können.

### 2.4 Stellungnahme


Das BPA hat mitgeteilt, dass es


- das IT-Sicherheitskonzept zu BPAvis fertiggestellt habe und

- es künftig fortschreiben werde.


Das _Audit Log_ hatte es aus Gründen des Datenschutzes deaktiviert. Es werde diese Funktion
künftig in allen HANA Datenbanken des BPA aktivieren.

### 2.5 Abschließende Würdigung


Das BPA setzt unsere Empfehlung bereits um.

# 3 IT-Betrieb

### 3.1 Sachverhalt


Das BPA bezeichnet BPAvis intern als Kriseninfrastruktur. Es diene der Sofortunterrichtung
aller politischen Entscheidungsträger rund um die Uhr (24/7). Es sei Gegenstand der Krisen­
pläne der Bundesregierung und essentieller Bestandteil der Krisenkommunikation (vgl.
Tz. 1.1). Den Schutzbedarf hinsichtlich des Schutzziels „Verfügbarkeit“ bewertete das BPA als

„hoch“.


12


#### 3.1.1 Service Level Agreement und Notfallkonzept

In seinem Betriebshandbuch legte das BPA fest, dass das System 24/7 verfügbar sein müsse.

Es strebte dabei eine Ausfallsicherheit von mehr als 99,7 % an. Die Dauer einzelner Ausfälle

sollte maximal zwei Stunden betragen.


Die interne Hotline des Systems war montags bis freitags von je 09:00 bis 17:00 Uhr zu errei­

chen.


Ein _Service Level Agreement_ (SLA) zu BPAvis konnte uns das BPA nicht vorlegen. Für die Ba­
siskomponenten gebe es Supportverträge mit den jeweiligen Dienstleistern. Darin enthalten
seien auch SLA. Diese seien allerdings durch die BPA-internen Supportzeiten limitiert, da hier
die erste Aufnahme und Bewertung im Störungsfall erfolge. Das BPA stellte selbst fest, dass
sich die „sehr hohe Ausfallsicherheit“ durch den IT-Betrieb im eigenen Rechenzentrum mit
einem Cloud-Notfallsystem aus Verfügbarkeitsgründen als nicht ausreichend erwiesen habe.


Das IT-Grundschutz-Kompendium des BSI sieht vor, sowohl für Standard-IT [13] als auch für
Cloud-Dienste [14] Notfallkonzepte zu erstellen. Das BSI stellt dazu einen eigenen Standard [15]
bereit: Demnach bestehen Notfallkonzepte aus einem Notfallvorsorgekonzept und einem

Notfallhandbuch.


Das BPA konnte uns weder ein Notfallkonzept zu BPAvis noch für das Cloud-Notfallsystem
vorlegen. Es übermittelte lediglich ein Dokument, das beschrieb, welche Arbeitsschritte bei
einem Ausfall durchzuführen wären („alternativer Workflow“).

#### 3.1.2 Hochverfügbarkeit


Das BSI definiert „Hochverfügbarkeit“ als eine Mindestverfügbarkeit von 99,99 % [16] .


In seinem IT-RK 2024 legte das BPA dar, es werde BPAvis georedundant ausbauen, um Hoch­
verfügbarkeit zu gewährleisten.

### 3.2 Würdigung


Der IT-Betrieb von BPAvis hat die Krisenkommunikation der Bundesregierung gefährdet. Bei
einem System, das 24/7 verfügbar sein muss, sind Servicezeiten innerhalb der „normalen
Dienstzeit“ inakzeptabel. Dem BPA ist dieser Mangel seit Jahren bekannt. Es hat ihn dennoch
bisher nicht abgestellt.


13 IT-Grundschutz-Kompendium, OPS.1.1.1.A3 (Erstellen von Betriebshandbüchern für die betriebene IT).
14 IT-Grundschutz-Kompendium, OPS.2.2.A11 (Erstellung eines Notfallkonzeptes für einen Cloud-Dienst).

15
BSI-Standard 200-4, _Business Continuity Management_ .
16 Hochverfügbarkeitskompendium des BSI, Band G, S. 31.


13


Das BPA hat versäumt, ein SLA für BPAvis zu vereinbaren. Damit ist nicht sichergestellt, dass

es Fehler in BPAvis zeitnah beheben kann.


Die fehlenden Notfallkonzepte für BPAvis und das Cloud-Notfallsystem haben zudem den er­
folgreichen Wiederanlauf des Systems gefährdet.


Wir halten es angesichts der Servicezeiten von BPAvis nicht für realistisch, dass das BPA für
BPAvis „Hochverfügbarkeit“ anstrebt.

### 3.3 Empfehlung


Für den IT-Betrieb von BPAvis als „Kriseninfrastruktur“ hat das BPA die Servicezeiten der in­
ternen Hotline auszuweiten. Dabei hat es auch zu prüfen, ob hierzu eine 24/7-Verfügbarkeit
erforderlich ist. Um die Verfügbarkeit der Hotline zu verbessern, könnte das BPA z. B. ausge­
wählte Beschäftigte seines Lagezentrums fortbilden. Es sollte für BPAvis zeitnah ein SLA ver­
einbaren, mit dem es die im Betriebshandbuch angegebenen Anforderungen auch erfüllen

kann.


Das BPA sollte für BPAvis und sein Cloud-Notfallsystem jeweils eigene Notfallkonzepte dem
BSI-Standard 200-4 entsprechend erstellen. Diese sollten über das bestehende „Workflow“Dokument hinausgehen.


Das BPA sollte seine verfügbaren Ressourcen zunächst dafür vorsehen,


- die von uns festgestellten Mängel schnellstmöglich abzustellen und

- die im Betriebshandbuch angedachte Verfügbarkeit sicherzustellen.

### 3.4 Stellungnahme


Das BPA hat dargestellt, es prüfe,


- für BPAvis SLA zu vereinbaren,

- die fehlenden Notfallkonzepte zu erstellen und

- die Servicezeiten der Hotline auszuweiten.


Unserer Empfehlung, ausgewählte Beschäftigte des Lagezentrums zur Fachadministration
fortzubilden, könne es nicht folgen. Für diesen Fall müsste es aufgrund des Schichtdienstes
_alle_ Beschäftigten des Lagezentrums fortbilden. Dies wirke sich möglicherweise auf die tarif­
liche Eingruppierung der Beschäftigten aus. Die hohe Verfügbarkeit des dazugehörigen Ge­
schäftsprozesses „Medienlage“ stelle es durch den parallelen und weitgehend unabhängigen

Betrieb von BPAvis


- im Rechenzentrum Berlin,


14


- dem Cloud-gestützten Notfallsystem sowie

- perspektivisch einer georedundanten Instanz von BPAvis im Rechenzentrum Bonn


sicher. In einer Krise hingegen könne es über organisatorische Regelungen längere Service­
zeiten ermöglichen.

### 3.5 Abschließende Würdigung


Das BPA will unseren Empfehlungen zu den SLA und den Notfallkonzepten folgen. Die Hin­
weise des BPA zur Eingruppierung seiner Beschäftigten sind nachvollziehbar. Das BPA sollte
weiter prüfen, wie es die Servicezeiten der Fachadministration auch für den Regelbetrieb

ausweiten kann.

# 4 Wirtschaftlichkeit

### 4.1 Sachverhalt


Nach § 7 Absatz 2 Satz 1 BHO sind für jede finanzwirksame Maßnahme in der Bundesverwal­
tung angemessene Wirtschaftlichkeitsuntersuchungen (WU) durchzuführen. Eine WU dient
dabei auch als Planungsinstrument. Bei IT-Verfahren bietet sich dafür eine WiBe gemäß den
Vorgaben [17] des Beauftragten der Bundesregierung für Informationstechnik an. Bei umfang­
reichen Maßnahmen mit hohen Ausgaben ist eine WiBe unabhängig von dem damit verbun­
denen Aufwand immer erforderlich. [18] Abhängig vom zeitlichen und inhaltlichen Umfang der
Maßnahmen sind weitere Versionen der WiBe als begleitende Erfolgskontrollen während
der Realisierung durchzuführen.


Die Projektverantwortlichen müssen sämtliche Alternativen auf die Zielerreichung hin über­
prüfen. Dabei müssen sie die Gründe für ausgeschlossene Alternativen dokumentieren. Zu­
vor müssen sie überprüfbare Ziele festlegen. Die Ziele sind mit geeigneten Indikatoren zu un­
terlegen, welche gemäß SMART-Konzept [19] zu konkretisieren sind. Die so konkretisierten
Ziele bilden auch eine wesentliche Grundlage für begleitende und abschließende Erfolgskon­
trollen. [20]


17 Fachkonzept WiBe 5.0 „Konzept zur Durchführung von Wirtschaftlichkeitsbetrachtungen in der Bundesver­


­
[waltung, insbesondere beim Einsatz der IT“, https://www.cio.bund.de/SharedDocs/down](https://www.cio.bund.de/SharedDocs/downloads/Webs/CIO/DE/digitale-loesungen/it-beschaffung/wirtschaftlichkeitsbetrachtung/wibe5-0/wibe-fachkonzept-5-0.pdf)
[loads/Webs/CIO/DE/digitale-loesungen/it-beschaffung/wirtschaftlichkeitsbetrachtung/wibe5-0/wibe-fach­](https://www.cio.bund.de/SharedDocs/downloads/Webs/CIO/DE/digitale-loesungen/it-beschaffung/wirtschaftlichkeitsbetrachtung/wibe5-0/wibe-fachkonzept-5-0.pdf)
[konzept-5-0.pdf, zuletzt aufgerufen am 13. Februar 2025.](https://www.cio.bund.de/SharedDocs/downloads/Webs/CIO/DE/digitale-loesungen/it-beschaffung/wirtschaftlichkeitsbetrachtung/wibe5-0/wibe-fachkonzept-5-0.pdf)
18 Ebenda.

19 ­
[https://www.orghandbuch.de/Webs/OHB/DE/OrganisationshandbuchNEU/4_MethodenUndTechni](https://www.orghandbuch.de/Webs/OHB/DE/OrganisationshandbuchNEU/4_MethodenUndTechniken/Methoden_A_bis_Z/SMART_Regel_Methode/SMART_Regel_Methode_node.html)

[ken/Methoden_A_bis_Z/SMART_Regel_Methode/SMART_Regel_Methode_node.html, zuletzt aufgerufen](https://www.orghandbuch.de/Webs/OHB/DE/OrganisationshandbuchNEU/4_MethodenUndTechniken/Methoden_A_bis_Z/SMART_Regel_Methode/SMART_Regel_Methode_node.html)

am 13. Februar 2025.
20 Fachkonzept WiBe 5.0.


15


In seinen IT-RK legte das BPA fest, dass für alle IT-Verfahren und -Vorhaben von finanzieller
Bedeutung WiBe vorliegen sollen. Die bisherigen Ausgaben für BPAvis belaufen sich auf
6,4 Mio. Euro (vgl. Tz. 1.3). In den Jahren 2024 bis 2027 rechnet das BPA mit weiteren Ausga­
ben von mindestens 4,4 Mio. Euro. Es beabsichtigt u. a., BPAvis neu zu entwickeln und in den
„NewsCenter-Verbund“ zu integrieren (vgl. Tz. 1.3). Die dazugehörigen Haushaltsmittelan­
sätze übernahm es unverändert aus einem Angebot des externen Dienstleisters.


Eine WiBe aus der Planungsphase sowie begleitende oder abschließende Erfolgskontrollen
zu BPAvis konnte uns das BPA nicht vorlegen. Es übermittelte dazu lediglich Testfallvorlagen

aus der Projektphase von BPAvis 2.0. Die entsprechenden Abschnitte in den IT-RK enthielten
allgemeine Aussagen wie „System unverzichtbar, Kriseninfrastruktur“. Das BPA konnte zu
BPAvis auch keine Aufrufstatistik vorlegen.

### 4.2 Würdigung


Die Vorgaben der BHO sind Grundpfeiler des Verwaltungshandelns. Sie sind für die ge­
samte Bundesverwaltung bindend – auch für „Kriseninfrastruktur“. Das BPA hat versäumt,
für BPAvis eine WiBe in der Planungsphase und begleitende sowie abschließende Erfolgskon­
trollen durchzuführen. Damit hat es gegen die haushaltsrechtlichen Grundsätze der Wirt­
schaftlichkeit und Sparsamkeit verstoßen.


Ohne WiBe kann die Verwaltung keine Aussage darüber treffen, ob Haushaltsmittel wirt­
schaftlich eingesetzt werden. Ob das BPA seine Haushaltsmittel bei BPAvis wirtschaftlich ein­
setzt, ist insbesondere bei einem Verfahren fraglich,


das knapp zwei Jahre nach Überführung in den Wirkbetrieb bereits neu entwickelt wer­

den soll und

- bei dem haushaltsbegründende Unterlagen im Wesentlichen auf Angeboten externer

Dienstleister basieren.


Die Wirtschaftlichkeit eines Projektes wie BPAvis 2.0 im Nachgang zu bewerten, wäre Auf­
gabe einer haushaltsrechtlich vorgeschriebenen Erfolgskontrolle gewesen: das BPA hätte so
„ _Lessons Learned_ “ aus seinem Projekt BPAvis 2.0 ziehen und diese bei der angedachten Wei­
terentwicklung berücksichtigen können. Eine Aufrufstatistik hätte dem BPA hier helfen kön­

nen,


einen Überblick über das Verhalten der Nutzerinnen und Nutzer zu gewinnen und

- BPAvis bedarfsgerecht weiterzuentwickeln.

### 4.3 Empfehlung


Das BPA hat für BPAvis zeitnah eine begleitende Erfolgskontrolle anhand konkreter, mit
messbaren Indikatoren unterlegter Ziele durchzuführen. Die Ergebnisse seiner


16


Erfolgskontrolle sollte es geeignet berücksichtigen, wenn es BPAvis weiterentwickelt und in
_NewsCenter_ integriert. Um BPAvis bedarfsgerecht weiterentwickeln zu können, sollte es
künftig eine Aufrufstatistik führen. Die Aufrufstatistik sollte das BPA bei seiner begleitenden
Erfolgskontrolle berücksichtigen.

### 4.4 Stellungnahme


Das BPA hat entgegnet, dass es die mit BPAvis verfolgten Ziele bereits in einer Leitungsvor­
lage aus dem Jahr 2019 hinreichend formuliert habe. Eine Erfolgskontrolle habe es innerhalb
von sechs Wochen nach der Überführung in den Wirkbetrieb durchgeführt. Es habe das da­
zugehörige Projekt erfolgreich abgeschlossen.

### 4.5 Abschließende Würdigung


Wir haben in unserer Prüfung alle Erfolgskontrollen von BPAvis angefordert. Das BPA konnte
uns weder begleitende noch abschließende Erfolgskontrollen vorlegen. Wir halten daher an
unseren Empfehlungen fest. Eine abschließende Erfolgskontrolle durchzuführen, ist haus­
haltsrechtlich vorgeschrieben. Den Punkt schließen wir ab.


Essers Fasswald


Beglaubigt: S. Erdmann, Tarifbeschäftigte


Wegen elektronischer Bearbeitung ohne Unterschrift und Dienstsiegelabdruck.


17


