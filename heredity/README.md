## Генетичний код
Створіть штучний інтелект для визначення вірогідності певної генетичної вади у людини:

## Очікуваний результат
```
** family0.csv **

Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
  Trait:
    True: 1.0000
    False: 0.0000
Lily:
  Gene:
    2: 0.0036
    1: 0.0136
    0: 0.9827
  Trait:
    True: 0.0000
    False: 1.0000

** family1.csv **

Arthur:
  Gene:
    2: 0.0329
    1: 0.1035
    0: 0.8636
  Trait:
    True: 0.0000
    False: 1.0000
Charlie:
  Gene:
    2: 0.0018
    1: 0.1331
    0: 0.8651
  Trait:
    True: 0.0000
    False: 1.0000
Fred:
  Gene:
    2: 0.0065
    1: 0.6486
    0: 0.3449
  Trait:
    True: 1.0000
    False: 0.0000
Ginny:
  Gene:
    2: 0.0027
    1: 0.1805
    0: 0.8168
  Trait:
    True: 0.1110
    False: 0.8890
Molly:
  Gene:
    2: 0.0329
    1: 0.1035
    0: 0.8636
  Trait:
    True: 0.0000
    False: 1.0000
Ron:
  Gene:
    2: 0.0027
    1: 0.1805
    0: 0.8168
  Trait:
    True: 0.1110
    False: 0.8890

** family2.csv **

Arthur:
  Gene:
    2: 0.0147
    1: 0.0344
    0: 0.9509
  Trait:
    True: 0.0000
    False: 1.0000
Hermione:
  Gene:
    2: 0.0608
    1: 0.1203
    0: 0.8189
  Trait:
    True: 0.0000
    False: 1.0000
Molly:
  Gene:
    2: 0.0404
    1: 0.0744
    0: 0.8852
  Trait:
    True: 0.0768
    False: 0.9232
Ron:
  Gene:
    2: 0.0043
    1: 0.2149
    0: 0.7808
  Trait:
    True: 0.0000
    False: 1.0000
Rose:
  Gene:
    2: 0.0088
    1: 0.7022
    0: 0.2890
  Trait:
    True: 1.0000
    False: 0.0000
```

## Технічні вимоги
Реалізуйте функції joint_probability, update і normalize.

Функція joint_probability повинна приймати список людей, дані про кількість копій кожного з генів у кожної людини, а також їхню схильність до генетичної вади. Функція має повертати об'єднану імовірність того, що всі ці події стануться.

- Функція приймає чотири значення: people, one_gene, two_gens та have_trait.
  Наприклад, якщо родина складається з Гаррі, Джеймса і Лілі, функція, де one_gene = {"Гаррі"}, two_genes = {"Джеймс"} і trait = {"Гаррі", "Джеймс"} має обчислити імовірність того, що в Лілі нуль копій гена, в Гаррі одна копію гена, а у Джеймса дві копії гена; Гаррі має генетичну ваду, Джеймс має ваду, а Лілі не має вади.
  Для тих, хто не має батьків у наборі даних, використовуйте розподіл імовірностей PROBS["gene"], щоб обчислити імовірність наявності в них певної кількості копій гена.
  Ті, хто має батьків у наборі даних, випадковим чином отримають один з двох батьківських генів, та існує імовірність PROBS["mutation"], що він мутує (не буде спричиняти генетичну ваду чи навпаки).
  Використовуйте розподіл імовірностей PROBS["trait"], щоби обчислити імовірність того, що людина має або не має генетичної вади.

- Функція update додає нову спільну імовірність розподілу до наявних розподілів імовірностей у відсотках.
  Функція приймає п'ять значень: probabilities, one_gene, two_genes, have_trait і p.
  Функція probabilities для кожної person (людини) має оновити розподіл генів probabilities[person]["gene"] і розподіл вад probabilities[person]["trait"], тобто додати значення p до відповідного значення у кожному розподілі. Всі інші значення слід залишити без змін.
  Наприклад, якщо «Гаррі» є і в two_genes, і в have_trait, p треба додати до probabilities["Harry"]["gene"][2] і до probabilities["Harry"]["trait"][True].
  Функція не має повертати жодного значення: вона має лише оновити перелік імовірностей.

- Функція normalize унормовує імовірності в переліку так, щоби при додаванні всіх, в сумі була 1 (а співвідношення залишалося незмінним).
  Функція приймає лише значення probabilities.
  Для обох розподілів кожної людини в probabilities ця функція має унормувати розподіли так, щоби сумма значень розподілу дорівнювали 1, а відносні значення не змінювалися.
  Наприклад, якщо probabilities["Harry"]["trait"][True] дорівнювали 0,1, а probabilities["Harry"]["trait"][False] дорівнювали 0,3, ваша функція має змінити (оновити) перше значення на 0,25, а друге – на 0,75: тепер сума цих чисел дорівнює 1, а друге значення все ще втричі більше за перше.
  Функція не повинна повертати жодного значення: вона має лише оновити перелік імовірностей (словник probabilities).
