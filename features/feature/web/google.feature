Feature: navegar por google

  @nasa @google
  Scenario: El navegador busca "nasa"
    Given Encender el navegador
    When  El navegador introduce la URL "https://google.es"
    And   Se visualiza la pagina de busqueda de google
    And   se abre una nueva pestana
    And   se selecciona la "1" pestana
    And   El navegador introduce la URL "https://starfriend.es"
    And   se selecciona la "1" pestana
    And   se cierra la pestana "1"
    And   se selecciona la "0" pestana
    And   Buscar en google por "nasa"
    And   Seleccionar el primer resultado en google
    Then  Comprobar que lleva a "https://www.nasa.gov/"
    And imprimir logs consola
 
  @google
  Scenario Outline:El navegador busca <palabra>
    Given Encender el navegador
    When  El navegador introduce la URL <urls>
    And   Se visualiza la pagina de busqueda de google
    And   Buscar en google por <palabra>
    And   Seleccionar el primer resultado en google
    Then  Comprobar que lleva a <urlrevisar>
    Examples:
    | urls                 | palabra          |  urlrevisar                   |
    | "https://google.es"  | "starfriend.es"  | "https://www.starfrie/"  |
