#
# _______________|  freqy : sort and order lines by frequency of appearance.
#
#           Usage:  freqy  [optional: file(s)]
#
#           Notes:  Will work in a pipe.
#                   Does not alter the file(s) themselves.
#
#    Dependencies:  none
#                 

#  CHANGE LOG  LATEST version available:   https://bitbucket.org/rsvp/gists/src
#
#  2012-02-15  Code review.
#  2009-04-30  First version of a very useful idiom.

# _______________     ::  BEGIN  Script ::::::::::::::::::::::::::::::::::::::::


cat "$@" | sort -f | uniq -c | sort -k 1nr -k 2f
#                                             ^second field, case-insensitive
#                                       ^highest numerical frequency first
#                         ^count frequency
#               ^-f means case-insensitive
#          ^needed to get similar lines adjacent to each other.
#   ^With no FILE, or when FILE is -, cat reads standard input.


exit 0
# _______________ EOS ::  END of Script ::::::::::::::::::::::::::::::::::::::::
