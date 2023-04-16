# ceneostraperN11
| Składowa | Nazwa | Selektor |
| --- | --- | --- |
| Opinia | Oinion /single opinion | div.js\_product-review |
| Identyfikator opinii | Opinion\_id | [data-entry-id] |
| Autor | Autor | span.user-post\_\_author-name |
| Rekomendacja | Recommendation | span.user-post\_\_author-recommendation \> em |
| Liczba gwiazdek | Score | Spam.user-post\_\_score-count |
| Czy opinia jest potwierdzona zakupem | Purchased | div.review-pz |
| Data wystawienia opinii | Opinion\_date | Span.user-post\_\_published \> time:nth-child(1)[datetime] |
| Data zakupu produktu | Purchuse\_date | Span.user-post\_\_published \> time:nth-child(1)[datetime] |
| Ile osób uznało opinie za przydatną | Likes | Buttton.vote-yes \> spanButtton.vote-yes[data-total-vote] |
| Ile osób uznało opinie za nieprzydatną | Dislikes | Buttton.vote-no \> spanButtton.vote-no[data-total-vote] |
| Treść opinii | Content | div.user-post\_\_text |
| Lista wad | Cons | div.review-feature\_\_title—negatives ~ div.review- |
| Lista zalet | pros | div.review-feature\_\_title—positives ~ div.review- |