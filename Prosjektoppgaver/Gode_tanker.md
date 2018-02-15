# Gode tanker

**I denne prosjektoppgaven skal du lage modeller, kjøre simuleringer og bygge et fysisk system. Oppgaven dekker store deler av kompetansemålene i faget [Programmering og modellering X](https://github.com/fagstoff/ProgMod/blob/master/Læreplan/kompetansemål.md). For å løse oppgaven må du ha god kjennskap til bruk av differensiallikninger og numerisk løsning av disse, og du må kunne grunnleggende programmering. Prosjektet bør gjennomføres som en gruppeoppgave.**

## Oppgave

Bygg et fysisk system av to tanker som oppfyller noen gitte spesifikasjoner. Bruk simuleringer for å designe systemet før det bygges. Verifiser korreksjonsfaktoren C for vann som strømmer fritt ut av et hull. Lag en visualisering med pygame som viser nivået i tankene i sanntid.

## Spesifikasjoner

* Begge tankene skal ha samme volum og skal inneholde like mye væske ved tiden t=0
* Volumet i hver enkelt tank skal være mellom 5-25 liter
* Tankene skal være sylindre eller prismer (kanner og bøtter er gode kandidater)
* Begge tankene skal ha et utløp i bunnen eller på siden nær bunnen
* Tankene skal fylles med vann
* Det skal ikke være noen tilførsel av væske i toppen av den første tanken
* Utløpet fra den første tanken i systemet skal renne inn i toppen av den andre tanken
* Utløpet av den andre tanken skal renne ut i en vask eller et sluk
* Væskestrømmen fra de to tankene skal være slik at den første tanken tømmes først
* Væskestrømmen fra den første tanken må være slik at den andre tanken ikke overfylles

## Ressurser

* Ta utgangspunkt i fagteksten [Tankmodell - To tanker](https://github.com/fagstoff/ProgMod/blob/master/Fagstoff/tankmodell_5.ipynb)
* Som et utgangspunkt for faktoren C kan du bruke verdien [0.61](https://www.usbr.gov/tsc/techreferences/mands/wmm/chap09_05.html)

## Innlevering

* Det skal tas opp en video av forsøket (eller forsøkene)
* Det skal lages en nettside som viser forsøket og resultatet av simuleringene
* Nettsiden skal også inneholde en kort introduksjon til matematiske modeller og en vurdering av resultatene
* Programkoden for simulering og visualisering skal gjøres tilgjengelig på nettsiden (valgfri lisens)

## Vurderingskriterier

### Høy måloppnåelse

* Det ferdige systemet fyller alle kravene som er gitt i spesifikasjonen
* Simuleringen gir en god tilnærming til hvordan det ferdige systemet oppfører seg
* Simuleringsprogrammet er strukturert og ryddig, med teknisk gode løsninger og god dokumentasjon
* Det kommer tydelig fram i rapporten hvilke forenklinger og antakelser som er gjort i modellen
* +++

### Middels måloppnåelse

todo...

### Lav måloppnåelse

todo...

## Kompetansemål

Prosjektet dekker følgende [kompetansemål fra læreplanen i faget](https://github.com/fagstoff/ProgMod/blob/master/Læreplan/kompetansemål.md):

### Grunnleggende programmering

* omgjøre problemstillinger til konkrete delproblemer, vurdere hvilke delproblemer som lar seg løse digitalt, og utforme løsninger for disse
* bruke grunnleggende programmering som variabler, datatyper, løkker, tester, plotting, tilfeldige tall, funksjoner og enkel brukerinteraksjon
* lage strukturerte og oversiktlige programmer med hensiktsmessige kommentarer

### Matematiske metoder

* lage programskisser og algoritmer med utgangspunkt i et matematisk problem
* bruke og utlede numeriske metoder for å derivere og integrere funksjoner
* bruke og utlede numeriske metoder til å løse differensiallikninger

### Modellering

* utforme matematiske modeller med utgangspunkt i praktiske problemstillinger og vurdere modellene
* gjøre rede for modellbegrepet og drøfte ulemper og fordeler ved noen modeller
* sammenligne resultater fra simuleringer med eksperimentelle data
* planlegge, utføre, drøfte og presentere et selvstendig arbeid knyttet til modellering


---
_Denne oppgaven er laget av [bitjungle](https://github.com/bitjungle). Oppgaven er lisensiert under en [Creative Commons Navngivelse-DelPåSammeVilkår 4.0 Internasjonal lisens.
](http://creativecommons.org/licenses/by-sa/4.0/)_
