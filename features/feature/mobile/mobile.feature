Feature: mobile

  Background:
    Given AppMobile Cerrar Popup
    And Comprobar fecha

  @mobile @validate
  Scenario:validacion del teclado
    When comprueba todos los botones
    And  presione el numero "1234567890.1234"
    Then el resultado tiene que ser "1234567890.1234"

