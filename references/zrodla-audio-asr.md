# Źródła audio-wideo i własne transkrypcje ASR

## Weryfikacja nagrania przed cytowaniem

- Istnienie nagrania i tożsamość kanału potwierdzaj przez YouTube oEmbed:
  `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<ID>&format=json`
  — zwraca JSON z `title` i `author_name`; HTTP 404 = nagranie nie istnieje.
  To najtańszy test: nie wymaga otwierania strony ani omijania zgód wiekowych.
- Kanał fanowski lub poświęcony osobie (wzorzec „<Imię Nazwisko> - <temat>") NIE dowodzi,
  że nagranie pochodzi od tej osoby. Zanim cytingujesz wypowiedź jako jej własną,
  potwierdź tożsamość głosu drugim źródłem (serwis, który relacjonował nagranie,
  oficjalny kanał, odczyt metadanych).
- Podcasty spoza YouTube: strona nadawcy zwykle nie ma transkrypcji, ale osadza URL
  audio w payloadzie RSC/JSON (`self.__next_f.push`, pole `audioUrl`). Grepuj surowy HTML
  na `.mp3` — nie ekstrakt tekstowy.

## Własna transkrypcja ASR jako źródło cytowań

- Zrób timestampowany transkrypt (workflow: skill `audio-transcription-cpu`; medium,
  nie small — nazwy własne), zapisz w repozytorium i w opisie źródła podaj ścieżkę
  do pliku + zapis „timestampy wg tego transkryptu”.
- Nazwy własne, których ASR nie rozpoznał, oznaczaj jawnie (ASR) i NIE poprawiaj
  z pamięci: błędnie „skorygowana” nazwa własna w przypisie jest trudniejsza
  do wychwycenia niż jawna flaga. Znane korekty potwierdzaj osobnym źródłem.
- Przy cytatach dosłownych (w cudzysłowie) odsłuchaj fragment przed publikacją —
  transkrypt ASR nie jest wiarygodny dla dosłownego brzmienia (interpunkcja,
  rozdzielanie zdań, liczebniki).
- W dokumentach analitycznych (MEMO/strategie) podawaj timestampy przy każdej tezie;
  w hasłach Wikipedii cytuj nagranie jak zwykłe źródło (data, nadawca, minuta),
  a timestampy trzymaj w transkrypcie.
