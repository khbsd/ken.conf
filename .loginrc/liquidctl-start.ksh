#!/bin/ksh
liquidctl --match Hydro initialize --pump-mode=performance &
liquidctl --match Hydro set fan speed 55 &

