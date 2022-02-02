That popular online word game Guesser
==============


This is a fairly simple tool for guessing at that popular online word game

## Requirements:

* Python3

## How to run:

To automate a single game, run the command like so

```
python3 guesser.py -a
```

The program will attempt a random first guess, Enter that into the game.  It
will then ask for the result.  For each character that is not in the word,
enter ".", If the square is yellow, enter a "y", and if the square is green,
enter a "g"

For example, if the guess was the word "joist", and the results were, grey,
green, green, green, green.  Enter ".gggg'.  The possible choices will then be
output, along with what should be the next guess, which may be the word
"moist",  Enter that word in to that popular online word game, and if the word
is guessed, enter "ggggg"

### Advanced usage

The tool also supports supplying a custom regex, and will filter the word list
via the regex.

```
python3 guesser.py -p <regex>
```

For example, to search for all words with the second letter "a" and the last
letter "h" and you know a "q" isn't  in the word, you could enter something
like

```
python3 guesser.py -p '[^q]a[^q][^q]h'
```

### Example

~~~
$ python3 guesser.py -a
Guess: pygmy
Enter result: (./y/g for each position): .y..g
Remaining words abbey, allay, alley, alloy, annoy, array, artsy, assay, aunty, badly, batty, bawdy, beady, beefy, belly, berry, biddy, billy, bitty, bobby, boney, booby, booty, boozy, bossy, briny, buddy, bulky, bully, bunny, burly, bushy, cabby, caddy, candy, canny, carry, catty, corny, covey, coyly, crazy, crony, curly, curry, curvy, daddy, daily, dairy, daisy, dally, dandy, decay, decoy, decry, deity, delay, derby, diary, dicey, dilly, dirty, ditty, dizzy, dolly, dowdy, downy, dowry, dryly, duchy, dully, dusky, dusty, early, ebony, edify, enjoy, entry, envoy, essay, every, fairy, fancy, fanny, fatty, ferry, fiery, fifty, filly, fishy, fizzy, flaky, folly, foray, forty, fully, funky, funny, furry, fussy, fuzzy, hairy, handy, hardy, harry, hasty, heady, heavy, hefty, hilly, hobby, holly, honey, horny, hotly, howdy, hunky, hurry, husky, hussy, icily, inlay, irony, itchy, ivory, jazzy, jelly, jerky, jetty, jiffy, jolly, juicy, kinky, kitty, lanky, leafy, leaky, leery, lefty, lobby, lofty, lorry, lousy, lowly, lucky, lusty, nanny, nasty, needy, nerdy, newly, ninny, nobly, noisy, nosey, nutty, oddly, ovary, query, rainy, rally, randy, ratty, ready, reedy, relay, retry, risky, rocky, rowdy, ruddy, rusty, sadly, sally, salty, sandy, sassy, saucy, savoy, savvy, scaly, scary, seedy, shady, shaky, shiny, showy, shyly, silky, silly, sissy, sixty, slyly, snaky, snowy, sooty, sorry, stony, story, stray, study, sulky, sully, sunny, surly, tabby, tacky, taffy, tally, tardy, tasty, tatty, tawny, teary, teddy, testy, today, toddy, truly, unify, unity, wacky, warty, weary, weedy, whiny, willy, windy, witty, woody, wooly, woozy, wordy, worry, wryly, zesty
Next guess is oddly
Enter result: (./y/g for each position): ....g
Remaining words abbey, array, artsy, assay, aunty, batty, beefy, berry, bitty, briny, bunny, bushy, cabby, canny, carry, catty, crazy, curry, curvy, entry, essay, every, fairy, fancy, fanny, fatty, ferry, fiery, fifty, fishy, fizzy, funky, funny, furry, fussy, fuzzy, hairy, harry, hasty, heavy, hefty, hunky, hurry, husky, hussy, itchy, jazzy, jerky, jetty, jiffy, juicy, kinky, kitty, nanny, nasty, ninny, nutty, query, rainy, ratty, retry, risky, rusty, sassy, saucy, savvy, scary, shaky, shiny, sissy, sixty, snaky, stray, sunny, tabby, tacky, taffy, tasty, tatty, tawny, teary, testy, unify, unity, wacky, warty, weary, whiny, witty, zesty
Next guess is hasty
Enter result: (./y/g for each position): ..ggg
Remaining words rusty, testy, zesty
Next guess is zesty
Enter result: (./y/g for each position): ggggg
~~~
