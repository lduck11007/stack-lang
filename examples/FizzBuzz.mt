100 VAR loop .
1 VAR i .

FOR loop
    || VAR ln .
    i 5 % 0 == 
    IF : .
        ln |Buzz| + VAR ln .
    ENDIF
    i 3 % 0 ==
    IF : .
        ln |Fizz| + VAR ln .
    ENDIF
    ln || ==
    IF : .
        i PRINT .
    ENDIF
    ln || !=
    IF : .
        ln PRINT .
    ENDIF
i 1 + VAR i .
ENDFOR