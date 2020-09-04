def solveWithEuler(dumpFile,stepsNumber,stepSize,a,y_old,z_old):
    '''
        solveWithEuler(dumpFile,stepsNumber,stepSize,a,y_old,z_old)

        This function compute and write the numerical
        solution of the equation (usign Euler's method)

            d**2y/d**2+ay=0                 (1)

        in dumpFile. We rewrite equation (1) as a system of two equations
        of degree one.

            dy/dx = z                       (2)
            dz/dx = -a*y                    (3)

        Euler's mehod solves diferential equations of degree one of the form:

            dy/dx = f(x,y)                  (4)

        using the next equation

            y = y_old + h*f(x_old,y_old)    (5)


        function        |type        |description
        parameter       |            |
                        |            |
        dumpFile        |string      | file where we will write the computation
        stepsNumber     |int         | number of steps
        stepSize        |float       | small increment in each step
        a               |float       | parameter in equation (1)
        y_old           |float       | initial value
        z_old           |float       | initial value
    '''
    file = open(dumpFile,"w") # the results will be stored in a file, old school way
    file.write("time,theta\n")

    y = y_old
    z = z_old

    for i in range(0,stepsNumber):
        x = i*stepSize # time will increase in h size steps
        y_old = y # value holder, because we need to actualize phi and theta simultaneusly
        z_old = z # value holder
        y = y_old + stepSize*z_old # theta actualization
        z = z_old - stepSize*a*y_old # phi actualization
        file.write("%f,%f\n"%(x,y)) # saving the result in the file

    file.close()
