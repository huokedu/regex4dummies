__author__ = 'Vale Tolpegin'

"""

Class information:

- name: main
- version: 1.3.4

"""

class main:
    # Global variables
    global overall_score
    global pattern_score
    global pattern_score_info
    global nltk_score
    global nltk_score_info
    global nlpnet_score
    global nlpnet_score_info

    # Constructor
    def __init__( self, *args, **kwargs ):
        # Getting global variables
        global overall_score
        global pattern_score
        global pattern_score_info
        global nltk_score
        global nltk_score_info
        global nlpnet_score
        global nlpnet_score_info

        # Displaying current message saying the example does not work yet
        print ""
        print "This is currently under development....Please check back soon for a working version."
        print ""

        return

        # Currently implemented functions that will be tested
        # This program performs a number of accuracy tests against the library. THey are:
        # 1. Each individual parser is tested
        #   a. Are the subject, verb, object, and prepositional phrases properly identified?
        #   b. Are the applicability score and the reliability score properly calculated?
        #   c. Are all of the patterns identified?
        # 2. All 3 parsers in one function call
        #   a. Are all of the patterns identified?
        #   b. Are the subject, verb, object, and prepositional phrases properly identified?
        #   c. Are the applicability score and the reliability score properly calculated?

        # Functions to be implemented that will be tested
        # 3. FreqDist to determine the possible topics that all to the strings relate to
        # 4. Topics for each pattern is correctly identified

        # Weighting of each aspect of the final score
        # Test-Set #1: 40%
        # Test-Set #2: 40%
        # Test-Set #3: 10%
        # Test-Set #4: 10%
        # The test sets total up to 100%, giving a complete score. This score is meant to represent
        #   how important each aspect of the library is relative to the other aspects of the library.

        print ""
        print "*" * 75
        print "regex4dummies Accuracy Tester"
        print ""
        print "Each test is valued in the following way ( 0 - 100 ): "
        print "* 100 - 90     : regex4dummies is consistently performing well and should be able to handle complex data"
        print "* 89 - 80      : regex4dummies is performing well, but does not perform that way consistently and cannot handle very complicated data"
        print "* 79 - 70      : regex4dummies is lacking in performance consistently and is not capable of parsing compex strings"
        print "* 69 and below : regex4dummies is doing very poorly and is considered still under development. It should not be used by anyone except developers"
        print "*" * 75
        print ""
        print "***Beginning Tests***"

        # Completing tests
        self.complete_tests()

        print "***Tests Completed***"
        print ""
        print ""
        print "***Score information***"
        print "Overall Score : " + str( overall_score )
        print ""
        print "NLTK Score    : " + str( nltk_score )
        print "Pattern Score : " + str( pattern_score )
        print "nlpnet Score  : " + str( nlpnet_score )
        print ""

        # Showing other test-related information
        print "NLTK test details:"
        print nltk_score_info
        print ""

        print "Pattern test details:"
        print pattern_score_info
        print ""

        print "nlpnet test details:"
        print nlpnet_score_info
        print ""

        print ""

    # This function will perform the above tests, and set the appropriate variables with test information
    def complete_tests( self ):
        # Getting global variables
        global overall_score
        global pattern_score
        global pattern_score_info
        global nltk_score
        global nltk_score_info
        global nlpnet_score
        global nlpnet_score_info

        # Setting all of the scores to restart
        overall_score = 0
        nltk_score    = 0
        pattern_score = 0
        nlpnet_score  = 0

        nltk_score_info    = ""
        pattern_score_info = ""
        nlpnet_score_info  = ""

if __name__ == '__main__':
    main()
