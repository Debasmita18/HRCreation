## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## leaves
* leave
  - utter_ask_name
* leave{"name":"Debasmita"}
  - slot{"name":"Debasmita"}
  - action_leave
  - slot{"name":"Debasmita"}
* leave{"name":"Akoparna"}
  - slot{"name":"Akoparna"}
  - action_leave
  - slot{"name":"Akoparna"}
* leave{"name":"Ankita"}
  - slot{"name":"Ankita"}
  - action_leave
  - slot{"name":"Ankita"}
  
## leave_application
* applyleave
  - utter_ask_id
* employee_id
  - slot{"ids":"102"}
  - action_days
* no_of_leaves
  - slot{"days":"2"}
  - action_leaves_submit
> Check_leaves_details

## affirm_path
> Check_leaves_details
* affirm
  - action_submit

  

## frequents
* faq
  - utter_ask_faq

## type_leaves
* leave_types
  - utter_types

## holidays_details
* holidays
  - utter_holidays_types

## sick_leave
* sl
  - utter_sleave

## casual_leave
* cl
  - utter_cleave
  
## thankyou
* thanks
  - utter_return
  
  
  
  
  
  
  