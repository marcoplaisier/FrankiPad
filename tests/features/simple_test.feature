Feature:
  Scenario: see if travis works
    Given we have behaved installed
    When we build a test
    Then behave will run it