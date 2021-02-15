Feature: navegar por google

  @game
  Scenario Outline: Listo para ser el mas rapido
    Given Encender el navegador
    When  El navegador introduce la URL <web_site>
    And   El navegador espera "3" segundos
    And   Comprobar que lleva a <web_site>
    And   Iniciar juego

    Examples:
      | web_site                          |
      | "https://zzzscore.com/color/en/#" |