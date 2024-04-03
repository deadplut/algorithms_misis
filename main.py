from algo_1_group import BubleSort, SimpleInsertsSort, SimpleSelectSort, DwarfSort
from algo_2group import PyramidSort, TournamentSort, ShellSort
from algorithms import MergeSort, QuickSort, MSDSort, LSDSort

output_file = 'results.txt'

# a = ShellSort(output_file)
#
#
# a.run_tests()







########################
## Первая группа
##################


# a = BubleSort('results_buble.txt')
# a.run_tests()
# b = SimpleInsertsSort('results_simple_inserts.txt')
# b.run_tests()
# # c = SimpleSelectSort(output_file)
# c = SimpleSelectSort('results_simple_select.txt')
# c.run_tests()
# d = DwarfSort('results_dwarf.txt')
# d.run_tests()


############################
## Вторая группа
#############################

# a = ShellSort('results_Shell.txt')
# a.run_tests()
# b = PyramidSort('results_Pyrami.txt')
# b.run_tests()
# c= TournamentSort('results_Tournament.txt')
# c.run_tests()

############################
## Третья группа
#############################

# a = MergeSort(output_file) #done
# a.run_tests()
#
# a = QuickSort(output_file) #done
# a.run_tests()

a = MSDSort('results_MSDSort.txt')
a.run_tests()
b = LSDSort('results_LSDSort.txt')
b.run_tests()