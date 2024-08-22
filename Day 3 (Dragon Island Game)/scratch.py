print(r'''                                        ,   ,
                                        $,  $,     ,
                                        "ss.$ss. .s'
                                ,     .ss$$$$$$$$$$s,
                                $. s$$$$$$$$$$$$$$`$$Ss
                                "$$$$$$$$$$$$$$$$$$o$$$       ,
                               s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s
                              s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,
                              s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"
                             s$$$$$$$$$$'         `"""ss"$"$s""
                             s$$$$$$$$$$,              `"""""$  .s$$s
                             s$$$$$$$$$$$$s,...               `s$$'  `
                         `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                           `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                 "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                  "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $
                                   $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                  $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'
                             ,   ,"     '  $$$$$$$$$$$$$$$$####s
                             $.          .s$$$$$$$$$$$$$$$$$####"
                 ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                 $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                 Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                  "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
           ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
           $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
           $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
            "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
              $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
   )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
  ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$
  ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
 (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
 )  ( (       $$"$$$$$$$$$$$#####.$$$$$###'                .###$$$$$$$$$$"
 (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
 ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
(   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"
(   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,
 )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$
  (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        '
    \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
        `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
            `"""""""""""""'         '           '           '
   ''')
print("Welcome to the Dragon Island")
print("Your mission is to find the treasure on this Island")
a=input('You are at a crossroad, where do you want to go? "Left" or "Right"').lower()
if a=="left":
    b=input('You see the dragon far away will you fight him now?\n'
            'Type "Yes" to fight.\n'
            'Type "run" to go away\n').lower()
    if b=="run":
        c=input('You arrive at the Dragon Temple.\n'
                'You see a sword and a corrupted axe.\n'
                'Type "sword" to pick sword.\n'
                'Type "axe" to pick corrupted axe.\n').lower()
        if c=="sword":
            print("You have picked the right weapon.")
            d=input('You see the Dragon with fire shield around him.\n'
                'Choose the attack type you want to use on the dragon.\n'
                  ' "Water" , "Fire" or "Earth".\n ').lower()
            if d=="water":
                print("The Dragon has been slain!")
                print(r''' 
                        \`-\`-._
                         \` )`. `-.__      ,
      '' , . _       _,-._;'_,-`__,-'    ,/
     : `. ` , _' :- '--'._ ' `------._,-;'
      `- ,`- '            `--..__,,---' ''')
            else:
                print("You picked the wrong element type! \n You Died!")
        else:
            print("You got corrupted by the axe \n Game Over!")

    else:
        print("You dont have the power to conquer the dragon \n Game Over!")
else:
    print("You chose the wrong path \n Game Over!")