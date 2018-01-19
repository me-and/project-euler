#!/usr/bin/env bash
set -e

declare -A TESTS_AND_RESULTS=(
	[pe001.py]=233168
	[pe002.py]=4613732
	[pe003.py]=6857
	[pe004.py]=906609
	[pe005.py]=232792560
	[pe006.py]=25164150
	[pe007.py]=104743
	[pe008.py]=23514624000
	[pe009.py]=31875000
	[pe010.py]=142913828922
	[pe011.py]=70600674
	[pe012.py]=76576500
	[pe013.py]=5537376230
	[pe014.py]=837799
	[pe015.py]=137846528820
	[pe016.py]=1366
	[pe017.py]=21124
	[pe018.py]=1074
	[pe019.py]=171
	[pe020.py]=648
	[pe021.py]=31626
	[pe022.py]=871198282
	[pe023.py]=4179871
	[pe024.py]=2783915460
	[pe025.py]=4782
	[pe026.py]=983
	[pe027.py]=-59231
	[pe028.py]=669171001
	[pe029.py]=9183
	[pe030.py]=443839
	[pe031.py]=73682
	[pe032.py]=45228
	[pe033.py]=100
	[pe034.py]=40730
	[pe035.py]=55
	[pe036.py]=872187
	[pe037.py]=748317
	[pe038.py]=932718654
	[pe039.py]=840
	[pe040.py]=210
	[pe041.py]=7652413
	[pe042.py]=162
	[pe043.py]=16695334890
	[pe044.py]=5482660
	[pe045.py]=1533776805
	[pe046.py]=5777
	[pe047.py]=134043
	[pe048.py]=9110846700
	[pe049.py]=296962999629
	[pe050.py]=997651
	[pe051.py]=121313
	[pe052.py]=142857
	[pe053.py]=4075
	[pe054.py]=376
	[pe055.py]=249
	[pe056.py]=972
	[pe057.py]=153
	[pe058.py]=26241
	[pe059.py]=107359
	[pe060.py]=26033
	[pe065.py]=272
	[pe067.py]=7273
	[pe079.py]=73162890
	[pe081.py]=427337
	[pe089.py]=743
	[pe092.py]=8581146
	[pe097.py]=8739992577
	[pe099.py]=709
	[pe206.py]=1389019170
)

run_test () {
	test="$1"
	result="$2"
	output="$(./"$test")"
	if [[ "$output" != "$result" ]]; then
		echo >&2
		echo "Failed $test" >&2
		echo "Expected $result" >&2
		echo "Saw $output" >&2
		return 1
	fi
}

failures=0
for test in pe*.py; do
	echo -n .
	run_test "$test" "${TESTS_AND_RESULTS["$test"]}" || (( failures += 1 ))
done

exit "$failures"
