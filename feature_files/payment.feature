Feature: item_order
    Scenario: item_order
        Given User create driver
        And   User open url
        When  User enter mobile number '****' and password '****'
        And   User click add cart
        And   User click proceed to buy
        And   User select country name 'India'
        And   User select name 'Samrat Chakraborty'
        And   User select mobile no '9123990228'
        And   User select pincode '711101'
        And   User select Flat no '15/1'
        And   User select street 'sribas datta lane'
        And   User select landmark 'Thelasemia hospital'
        And   User select state
        And   User select address type
        And   User select use to address
        And   User select other upi '9123990224@sbi'
        Then  User close driver
