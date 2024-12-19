import numpy as np 
def init_pop(pop_size):#  (الي هو عايزه (اكريت كام روn هتاخد ال 
    # N shoud be even (rows of population)     n*8               
    return np.random.randint(8,size=(pop_size,8))# في ال 8 روز بتوعيpopulation هكريت عدد ال 
# al random give me num between 0 to 8-1=7
#random is a class, randint is a function i give a num it gives me a range between 0 and num-1
#8:range , popsize:num of rows ,8:num of columns
initial_population=init_pop(4)#num of rows=4 and store in initial_population 
print (initial_population)# كل القيم هتبقي من 1 لحد 7

# Methode to calculate Fitness by use population   
def calc_fitness(population):
    #بتوضح جوده الحل بتاعي ولازم تبقي كبيره
    fitness_values=[]#empty list to store fitness values for all initial population
    for x in population:#كل مره خد الرو الاول وبعدها التاني وهكذا
       #  بتاعتيpopulation بالوب ديه بلف علي ال
        penalty=0#same as the sum
        #عدد الكوينز الي ممكن اكلها
        for i in range(8):# بتشتغل علي الروز[0---7]
            r=x[i]# intial populationهيديني اول رقم في اول رو موجود في ال
            for j in range(8):# columnsبتشتغل علي ال 
              if i==j:
                #the first iteration i=0 and j=0 then i==j continue *not continue the code*,second iterationi=0 j=1 then not make continue
                continue
              d=abs(i-j)
              if x[j] in [r,r-d,r+d]:#check if there is a queen in the beside one and its upper and bottom
                penalty+=1
        fitness_values.append(penalty) #store penalty in the empty array[fitness values]
    return -1*np.array(fitness_values)
fitness_values=calc_fitness(initial_population)
print(fitness_values)

#Selection
def Selection(population,fitness_values):#population =rows=intial population /fitness_values array that we calculate above
   probs=fitness_values.copy()#[-14,-16,-18,-10]
   probs+=abs(probs.min())+1
   probs=probs/probs.sum()#calculate probabilities
   n=len(population)#N=4     len of intial population
   indices=np.arange(n)#indices=0,1,2,3
   selected_indices=np.random.choice(indices,size=n,p=probs)#indi=0,1,2,3 / size that i will work on it(4) /probabilities=50%,17%....
   #يقولي هنختار ايه بقي ال 3 ولا ال 2 وكده بقي حسب احتمال كل واحد فيهم
   salected_population=population[selected_indices]
   return salected_population
salected_population=Selection(initial_population,fitness_values)
print(salected_population)
#print(Selection(initial_population,fitness_values))

# Crossover
def CrossOver(Parent1,Parent2,pc):#pc : probability of crossover
   r=np.random.random()#random value between 0 & 1
   if r<pc:
      m=np.random.randint(1,8)# form 1 to 8-1=7
      Child1=np.concatenate([Parent1[:m],Parent2[m:]])#m-1
      Child2=np.concatenate([Parent2[:m],Parent1[m:]])
   else:
      Child1=Parent1.copy()
      Child2=Parent2.copy()
   return Child1,Child2   
# Parent1=salected_population[0]  
# Parent2=salected_population[1] 
# Child1 ,Child2 = CrossOver(Parent1,Parent2,PC=0.70)
# print(Parent1 ,'-->',Child1)
# print(Parent2 ,'-->',Child2)   

# Mutation
def mutation(individual,pm):#  individual =[5,2,1,5,0,3,1,2]---->[5,2,4,5,0,3,1,2]
   r=np.random.random()# range 0 to 1
   if r<pm:
      m=np.random.randint(8)#0 to 7   m=3
      individual[m]=np.random.randint(8)# individual [3]=0 to 6     say return 4
   return individual # [5,2,4,5,0,3,1,2]

#crossover&mutation
def crossover_mutation(salected_pop,pc,pm):
    n=len(salected_pop)
    new_pop= np.empty((n,8),dtype=int)#empty matrix /size =n*8/ data type = integer
    for i in range (0,n,2): # implement crossover/ by step 2/ i=0 then i=2
        Parent1=salected_pop[i]#parent 3
        Parent2=salected_pop[i+1]#parent 4
        Child1 ,Child2 = CrossOver(Parent1,Parent2,pc)
        new_pop[i]=Child1
        new_pop[i+1]=Child2
    for i in range (n):# implement mutation
        mutation(new_pop[i],pm)  
    return new_pop  

#8 Queens
def eight_queens (pop_size, max_generations, pc=0.7, pm=0.01):
    population = init_pop(pop_size) # random intial population   100 row & 8 columns
    best_fitness_overall = None # store best fitness
    for i_gen in range (max_generations) :
        fitness_values = calc_fitness(population)#[-18,-10,-4,-8]
        best_i = fitness_values.argmax()# ال اندكس  بتاع افضل(اكبر) قيمه للفيتنس موجوده عندي/  -4
        best_fitness = fitness_values[best_i]# -4
        if best_fitness_overall is None or best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            best_solution = population[best_i]
            print(f'\ri_gen ={i_gen:06}-f={-best_fitness_overall:03}', end='')#\r to delete the old and write the new ,end : to print in the same line..
            if best_fitness == 0:
              print('\nFound optimal solution')
              break
        selected_pop = Selection (population, fitness_values)
        population= crossover_mutation(selected_pop, pc, pm)
    print()
    print (best_solution)
eight_queens (pop_size=100, max_generations=10000,pc=0.7, pm=0.01)

print("hello")

