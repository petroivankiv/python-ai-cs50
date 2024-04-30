Напишіть штучний інтелект для створення кросвордів.

$ python generate.py data/structure1.txt data/words1.txt output.png


## Технічні вимоги

Завершіть реалізацію функцій enforce_node_consistency, revise, ac3, assignment_complete, consistent, order_domain_values, selected_unassigned_variable та backtrack у файлі generate.py, щоби ваш штучний інтелект генерував заповнені кросворди, якщо це можливо.

1. Функція enforce_node_consistency має оновити self.domains так, щоби кожна змінна мала вузлову сумісність.
  
2. Функція revise має зробити змінну x дугосумісною зі змінною y.
   
3. Функція ac3 має забезпечити дугосумісність  кросворда за допомогою алгоритму AC3. Як ви вже знаєте з лекції, щоби цього досягти, необхідно, аби всі значення з області визначення кожної змінної задовольняли бінарні обмеження цієї змінної.
   
4. Функція assignment_complete має (як зрозуміло з назви) перевіряти, чи завершене присвоєння (assignment).
   
5. Функція consistent має перевіряти, чи задане присвоєння сумісне.
   
6. Функція order_domain_values має повертати список всіх значень з області визначення var, впорядкованих відповідно до евристики найменш обмежених значень.
   
7. Функція select_unassigned_variable має повернути одну змінну кросворда, якій ще не присвоєно значення в assignment відповідно до евристики мінімального значення та евристики степеня.
   
8. Функція backtrack має отримувати часткове присвоєння (assignment) і, за допомогою пошуку з поверненням, повертати повне задовільне присвоєння змінних значенням, якщо це можливо.

Не слід більше нічого змінювати у generate.py, окрім функцій, зазначених у технічних вимогах. Однак ви можете створювати додаткові функції та / або імпортувати інші модулі стандартної бібліотеки Python. Також дозволяється імпортувати numpy або pandas, якщо ви володієте ними, будь-які інші сторонні модулі Python використовувати заборонено. Водночас немає потреби щось змінювати в crossword.py.