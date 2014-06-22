import solver
import grid
import checker

print 'hello'

end = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
gen = grid.generate()

for i in gen:
    print(i)

if checker.check_solution(gen):
    solver.puzz_astar(gen, end)


