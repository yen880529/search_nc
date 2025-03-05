import math

A=3
B=118
C=B+1 #139
D=59
E=25
F=45
G=1
H=C+(G/2) #140
I=1
J=C+I
K=35
L=(K/2)+I



reserved=1
blade_radius=0.8

reserved1=2.5








def calculate_all_1(A, B, C, D, E, reserved, blade_radius):

    # 1. 计算三角形ABC的角度
    def calculate_angles_ABC(A, B, C):
        # 使用余弦定理计算每个角度的余弦值
        angle_A_rad = math.acos((B**2 + C**2 - A**2) / (2 * B * C))
        angle_B_rad = math.acos((A**2 + C**2 - B**2) / (2 * A * C))
        angle_C_rad = math.acos((A**2 + B**2 - C**2) / (2 * A * B))

        # 将角度从弧度转换为度
        angle_A = math.degrees(angle_A_rad)
        angle_B = math.degrees(angle_B_rad)
        angle_C = math.degrees(angle_C_rad)
        return angle_A, angle_B, angle_C

    # 2. 计算角度 BDE
    def calculate_angles_BDE(B, D, E):
        angle_BDE_rad = math.asin((D + E) / B)
        angles_BDE = math.degrees(angle_BDE_rad)


        oil_Z1 = B * math.sin(math.radians(90-angles_BDE))






        return angles_BDE,oil_Z1

    # 3. 计算 A1 和 A2
    def angles_ACD(A, angle_C, angles_BDE):
        angle_F = angle_C + angles_BDE
        A1 = A * math.cos(math.radians(180 - angle_F))
        A2 = A * math.sin(math.radians(angle_F))
        return A1, A2

    # 4. 计算角度AA
    def AABB1A(A, B, C):
        angles_AA_rad = math.acos((B**2 + (C + A)**2 - (2 * A)**2) / (2 * B * (C + A)))
        angles_AA = math.degrees(angles_AA_rad)
        return angles_AA

    # 5. 计算 X 值
    def calculate_X(B, angles_AA):
        angle_BX = 180 - 90 - angles_AA
        X = B * math.cos(math.radians(angle_BX))
        return X , angle_BX

    # 6. 计算 Y 值
    def calculate_Y(C, B, angles_AA):
        Y = math.sqrt(math.pow(C,2) + math.pow(B, 2) - 2 * C * B * math.cos(math.radians(angles_AA)))
        return Y 

    # 7. 计算角 XY
    def angles_XY(X, Y):
        XY = math.sqrt(Y**2 - X**2)
        Z1 = math.asin(XY / Y)
        Z = math.degrees(Z1)
        return Z , XY

    # 8. 计算角度 AAY
    def angles_AAY(A, Y):
        AAY1 = math.acos(((2 * A)**2 + Y**2 - A**2) / (2 * Y * (2 * A)))
        AAY = math.degrees(AAY1)
        return AAY

    # 9. 计算 R2_X 和 R2_Y
    def angles_R2(angles_BDE, angles_AA, Z, AAY, A, reserved, blade_radius):
        AAX = 90 - angles_AA

        X1 = 180 - (angles_BDE + AAX + Z + AAY)
        
    
        R2_X = A * math.sin(math.radians(X1))
        R2_Y = A * math.cos(math.radians(X1))

        #第一刀
        R2_X_1 = (reserved + blade_radius) * math.sin(math.radians(X1))+blade_radius
        R2_Y_1 = (reserved + blade_radius) * math.cos(math.radians(X1))-blade_radius
        #第二刀
        R2_X_03 = (reserved-0.7 + blade_radius) * math.sin(math.radians(X1))+blade_radius
        R2_Y_03 = (reserved-0.7 + blade_radius) * math.cos(math.radians(X1))-blade_radius
        #第三刀
        R2_X_0 = (blade_radius) * math.sin(math.radians(X1))+blade_radius
        R2_Y_0 = (blade_radius) * math.cos(math.radians(X1))-blade_radius

        return R2_X, R2_Y, X1, AAX,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0

    # 10. 计算 R1_X 和 R1_Y
    def angles_R1(Y, AAY, X1, Z, reserved, blade_radius):
        X2 = 90 - X1 - AAY
        R1_X = Y * math.cos(math.radians(X2))
        R1_Y = Y * math.sin(math.radians(X2))
        R2 = 90 - (Z + AAY + X1)

        #第一刀
        R1_X_1 = (reserved + blade_radius) * math.sin(math.radians(R2))-blade_radius
        R1_Y_1 = (reserved + blade_radius) * math.cos(math.radians(R2))-blade_radius
        #第二刀
        R1_X_03 = (reserved-0.7 + blade_radius) * math.sin(math.radians(R2))-blade_radius
        R1_Y_03 = (reserved-0.7 + blade_radius) * math.cos(math.radians(R2))-blade_radius
        #第三刀
        R1_X_0 = (blade_radius) * math.sin(math.radians(R2))-blade_radius
        R1_Y_0 = (blade_radius) * math.cos(math.radians(R2))-blade_radius

        return R1_X, R1_Y, X2,R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0

    # 11. 计算 R3
    def angles_R3(Y, B, C, angles_BDE, AAY,reserved, blade_radius):
        angles_BX_rad = math.acos((Y**2 + B**2 - C**2) / (2 * Y * B))
        angles_BX = math.degrees(angles_BX_rad)
        X3 = 90 - (AAY + (angles_BX - angles_BDE))
        R3_X = A * math.cos(math.radians(X3))
        R3_Y = A * math.sin(math.radians(X3))

        #第一刀
        R3_X_1 = (reserved + blade_radius) * math.cos(math.radians(X3))-blade_radius
        R3_Y_1 = (reserved + blade_radius) * math.sin(math.radians(X3))+blade_radius

        #第二刀
        R3_X_03 = (reserved-0.7 + blade_radius) * math.cos(math.radians(X3))-blade_radius
        R3_Y_03 = (reserved-0.7 + blade_radius) * math.sin(math.radians(X3))+blade_radius

        #第三刀
        R3_X_0 = (blade_radius) * math.cos(math.radians(X3))-blade_radius
        R3_Y_0 = (blade_radius) * math.sin(math.radians(X3))+blade_radius

        return angles_BX, X3, R3_X, R3_Y , R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0

    # 12. 计算 R4
    def angles_R4(angles_AA,Y, angles_BX, angles_BDE,reserved, blade_radius):
        X4 = angles_BX - angles_BDE
        R4_X = Y * math.sin(math.radians(X4))
        R4_Y = Y * math.cos(math.radians(X4))
        R4 = 180-((90-X4)+angles_BX+angles_AA)

        #第一刀
        R4_X_1 = (reserved + blade_radius) * math.cos(math.radians(R4))-blade_radius
        R4_Y_1 = (reserved + blade_radius) * math.sin(math.radians(R4))-blade_radius
        #第二刀
        R4_X_03 = (reserved-0.7 + blade_radius) * math.cos(math.radians(R4))-blade_radius
        R4_Y_03 = (reserved-0.7 + blade_radius) * math.sin(math.radians(R4))-blade_radius
        #第三刀
        R4_X_0 = (blade_radius) * math.cos(math.radians(R4))-blade_radius
        R4_Y_0 = (blade_radius) * math.sin(math.radians(R4))-blade_radius

        return R4_X, R4_Y ,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0, R4,X4
    
    #13 計算第一個油溝的座標
    def oil_1_all(R1_X, R1_Y,R2_X, R2_Y,  R3_X, R3_Y,R4_X, R4_Y, R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0,R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0,E):
        #第一個油溝的R角第一點座標
        oil_R1_Z_1=E-R1_X-R1_X_1
        oil_R1_X_1=(oil_Z1+R1_Y-R1_Y_1)*2

        oil_R1_Z_03=E-R1_X-R1_X_03
        oil_R1_X_03=(oil_Z1+R1_Y-R1_Y_03)*2

        oil_R1_Z_0=E-R1_X-R1_X_0
        oil_R1_X_0=(oil_Z1+R1_Y-R1_Y_0)*2

        #第一個油溝的R角第二點座標
        oil_R2_Z_1=E-R2_X+R2_X_1
        oil_R2_X_1=(oil_Z1+R2_Y-R2_Y_1)*2

        oil_R2_Z_03=E-R2_X+R2_X_03
        oil_R2_X_03=(oil_Z1+R2_Y-R2_Y_03)*2

        oil_R2_Z_0=E-R2_X+R2_X_0
        oil_R2_X_0=(oil_Z1+R2_Y-R2_Y_0)*2

        #第一個油溝的R角第三點座標
        oil_R3_Z_1=E + R3_X - R3_X_1
        oil_R3_X_1=(oil_Z1 - R3_Y + R3_Y_1)*2

        oil_R3_Z_03=E + R3_X - R3_X_03
        oil_R3_X_03=(oil_Z1 - R3_Y + R3_Y_03)*2

        oil_R3_Z_0=E + R3_X - R3_X_0
        oil_R3_X_0=(oil_Z1 - R3_Y + R3_Y_0)*2


        #第一個油溝的R角第三點座標
        oil_R4_Z_1=E + R4_X - R4_X_1
        oil_R4_X_1=(oil_Z1 - R4_Y - R4_Y_1)*2

        oil_R4_Z_03=E + R4_X - R4_X_03
        oil_R4_X_03=(oil_Z1 - R4_Y - R4_Y_03)*2

        oil_R4_Z_0=E + R4_X - R4_X_0
        oil_R4_X_0=(oil_Z1 - R4_Y - R4_Y_0)*2

        return oil_R1_Z_1,oil_R1_X_1 , oil_R2_Z_1,oil_R2_X_1 , oil_R3_Z_1,oil_R3_X_1 , oil_R4_Z_1,oil_R4_X_1 , oil_R1_Z_03,oil_R1_X_03 , oil_R2_Z_03,oil_R2_X_03 , oil_R3_Z_03,oil_R3_X_03 , oil_R4_Z_03,oil_R4_X_03 , oil_R1_Z_0,oil_R1_X_0 , oil_R2_Z_0,oil_R2_X_0 , oil_R3_Z_0,oil_R3_X_0 , oil_R4_Z_0,oil_R4_X_0
    

       # 调用各个函数
    angles_ABC = calculate_angles_ABC(A, B, C)
    angles_BDE ,oil_Z1= calculate_angles_BDE(B, D, E)
    A1, A2 = angles_ACD(A, angles_ABC[2], angles_BDE)
    angles_AA = AABB1A(A, B, C)
    X,angle_BX = calculate_X(B, angles_AA)
    Y = calculate_Y(C, B, angles_AA)
    Z, XY = angles_XY(X, Y)
    AAY = angles_AAY(A, Y)
    R2_X, R2_Y, X1, AAX,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0= angles_R2(angles_BDE, angles_AA, Z, AAY, A, reserved, blade_radius)
    R1_X, R1_Y, X2,R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0 = angles_R1(Y, AAY, X1, Z, reserved, blade_radius)
    angles_BX, X3, R3_X, R3_Y , R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0 = angles_R3(Y, B, C, angles_BDE, AAY,reserved, blade_radius)
    R4_X, R4_Y ,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0, R4,X4= angles_R4(angles_AA,Y, angles_BX, angles_BDE,reserved, blade_radius)

    oil_R1_Z_1,oil_R1_X_1 , oil_R2_Z_1,oil_R2_X_1 , oil_R3_Z_1,oil_R3_X_1 , oil_R4_Z_1,oil_R4_X_1 , oil_R1_Z_03,oil_R1_X_03 , oil_R2_Z_03,oil_R2_X_03 , oil_R3_Z_03,oil_R3_X_03 , oil_R4_Z_03,oil_R4_X_03 , oil_R1_Z_0,oil_R1_X_0 , oil_R2_Z_0,oil_R2_X_0 , oil_R3_Z_0,oil_R3_X_0 , oil_R4_Z_0,oil_R4_X_0=oil_1_all(R1_X, R1_Y,R2_X, R2_Y,  R3_X, R3_Y,R4_X, R4_Y, R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0,R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0,E)

    #print(f"油溝1: {oil_R1_X_1:.2f},{oil_R1_Z_1:.2f}")
    #print(f"油溝2: {oil_R2_X_1:.2f},{oil_R2_Z_1:.2f}")
    #print(f"油溝3: {oil_R3_X_1:.2f},{oil_R3_Z_1:.2f}")
    #print(f"油溝4: {oil_R4_X_1:.2f},{oil_R4_Z_1:.2f}")

    #print(f"油溝1: {oil_R1_X_03:.2f},{oil_R1_Z_03:.2f}")
    #print(f"油溝2: {oil_R2_X_03:.2f},{oil_R2_Z_03:.2f}")
    #print(f"油溝3: {oil_R3_X_03:.2f},{oil_R3_Z_03:.2f}")
    #print(f"油溝4: {oil_R4_X_03:.2f},{oil_R4_Z_03:.2f}")

    #print(f"油溝1: {oil_R1_X_0:.2f},{oil_R1_Z_0:.2f}")
    #print(f"油溝2: {oil_R2_X_0:.2f},{oil_R2_Z_0:.2f}")
    #print(f"油溝3: {oil_R3_X_0:.2f},{oil_R3_Z_0:.2f}")
    #print(f"油溝4: {oil_R4_X_0:.2f},{oil_R4_Z_0:.2f}")

    #print(f"測試: {R1_X:.2f},{R1_Y:.2f}")

    #print(f"測試1: {X2:.2f}")
    #print(f"測試2: {X1:.2f}")

    #print(f"angles_AA: {angles_AA:.2f}")


    #print(f"X: {X:.2f}")
    #print(f"Y: {Y:.2f}")

    #print(f"XY: {Z:.2f}")






    #print(f"angles_BDE: {angles_BDE:.2f}")
    #print(f"AAX: {AAX:.2f}")






    oil_R1_Z_1,oil_R1_X_1 , oil_R2_Z_1,oil_R2_X_1 , oil_R3_Z_1,oil_R3_X_1 , oil_R4_Z_1,oil_R4_X_1 , oil_R1_Z_03,oil_R1_X_03 , oil_R2_Z_03,oil_R2_X_03 , oil_R3_Z_03,oil_R3_X_03 , oil_R4_Z_03,oil_R4_X_03 , oil_R1_Z_0,oil_R1_X_0 , oil_R2_Z_0,oil_R2_X_0 , oil_R3_Z_0,oil_R3_X_0 , oil_R4_Z_0,oil_R4_X_0=oil_1_all(R1_X, R1_Y,R2_X, R2_Y,  R3_X, R3_Y,R4_X, R4_Y, R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0,R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0,E)
    return oil_R1_Z_1,oil_R1_X_1 , oil_R2_Z_1,oil_R2_X_1 , oil_R3_Z_1,oil_R3_X_1 , oil_R4_Z_1,oil_R4_X_1 , oil_R1_Z_03,oil_R1_X_03 , oil_R2_Z_03,oil_R2_X_03 , oil_R3_Z_03,oil_R3_X_03 , oil_R4_Z_03,oil_R4_X_03 , oil_R1_Z_0,oil_R1_X_0 , oil_R2_Z_0,oil_R2_X_0 , oil_R3_Z_0,oil_R3_X_0 , oil_R4_Z_0,oil_R4_X_0
oil_R1_Z_1,oil_R1_X_1 , oil_R2_Z_1,oil_R2_X_1 , oil_R3_Z_1,oil_R3_X_1 , oil_R4_Z_1,oil_R4_X_1 , oil_R1_Z_03,oil_R1_X_03 , oil_R2_Z_03,oil_R2_X_03 , oil_R3_Z_03,oil_R3_X_03 , oil_R4_Z_03,oil_R4_X_03 , oil_R1_Z_0,oil_R1_X_0 , oil_R2_Z_0,oil_R2_X_0 , oil_R3_Z_0,oil_R3_X_0 , oil_R4_Z_0,oil_R4_X_0=calculate_all_1(A, B, C, D, E, reserved, blade_radius)
 








#calculate_all_1(A, B, C, D, E, reserved, blade_radius)

def calculate_all_2(A, B, C, D, F, reserved, blade_radius):
    # 1. 计算三角形ABC的角度
    def calculate_angles_ABC(A, B, C):
        # 使用余弦定理计算每个角度的余弦值
        angle_A_rad = math.acos((B**2 + C**2 - A**2) / (2 * B * C))
        angle_B_rad = math.acos((A**2 + C**2 - B**2) / (2 * A * C))
        angle_C_rad = math.acos((A**2 + B**2 - C**2) / (2 * A * B))

        # 将角度从弧度转换为度
        angle_A = math.degrees(angle_A_rad)
        angle_B = math.degrees(angle_B_rad)
        angle_C = math.degrees(angle_C_rad)
        return angle_A, angle_B, angle_C

    # 2. 计算角度 BDE
    def calculate_angles_BDE(B, D, F):
        angle_BDE_rad = math.asin((D + F) / B)
        angles_BDE = math.degrees(angle_BDE_rad)


        oil_Z1 = B * math.sin(math.radians(90-angles_BDE))






        return angles_BDE,oil_Z1

    # 3. 计算 A1 和 A2
    def angles_ACD(A, angle_C, angles_BDE):
        angle_F = angle_C + angles_BDE
        A1 = A * math.cos(math.radians(180 - angle_F))
        A2 = A * math.sin(math.radians(angle_F))
        return A1, A2

    # 4. 计算角度AA
    def AABB1A(A, B, C):
        angles_AA_rad = math.acos((B**2 + (C + A)**2 - (2 * A)**2) / (2 * B * (C + A)))
        angles_AA = math.degrees(angles_AA_rad)
        return angles_AA

    # 5. 计算 X 值
    def calculate_X(B, angles_AA):
        angle_BX = 180 - 90 - angles_AA
        X = B * math.cos(math.radians(angle_BX))
        return X

    # 6. 计算 Y 值
    def calculate_Y(C, B, angles_AA):
        Y = math.sqrt(math.pow(C,2) + math.pow(B, 2) - 2 * C * B * math.cos(math.radians(angles_AA)))
        return Y

    # 7. 计算角 XY
    def angles_XY(X, Y):
        XY = math.sqrt(Y**2 - X**2)
        Z1 = math.asin(XY / Y)
        Z = math.degrees(Z1)
        return Z 

    # 8. 计算角度 AAY
    def angles_AAY(A, Y):
        AAY1 = math.acos(((2 * A)**2 + Y**2 - A**2) / (2 * Y * (2 * A)))
        AAY = math.degrees(AAY1)
        return AAY

    # 9. 计算 R2_X 和 R2_Y
    def angles_R2(angles_BDE, angles_AA, Z, AAY, A, reserved, blade_radius):
        AAX = 90 - angles_AA
        X1 = 180 - (angles_BDE + AAX + Z + AAY)
        R2_X = A * math.sin(math.radians(X1))
        R2_Y = A * math.cos(math.radians(X1))

        #第一刀
        R2_X_1 = (reserved + blade_radius) * math.sin(math.radians(X1))+blade_radius
        R2_Y_1 = (reserved + blade_radius) * math.cos(math.radians(X1))-blade_radius
        #第二刀
        R2_X_03 = (reserved-0.7 + blade_radius) * math.sin(math.radians(X1))+blade_radius
        R2_Y_03 = (reserved-0.7 + blade_radius) * math.cos(math.radians(X1))-blade_radius
        #第三刀
        R2_X_0 = (blade_radius) * math.sin(math.radians(X1))+blade_radius
        R2_Y_0 = (blade_radius) * math.cos(math.radians(X1))-blade_radius

        return R2_X, R2_Y, X1, AAX,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0

    # 10. 计算 R1_X 和 R1_Y
    def angles_R1(Y, AAY, X1, Z, reserved, blade_radius):
        X2 = 90 - X1 - AAY
        R1_X = Y * math.cos(math.radians(X2))
        R1_Y = Y * math.sin(math.radians(X2))
        R2 = 90 - (Z + AAY + X1)

        #第一刀
        R1_X_1 = (reserved + blade_radius) * math.sin(math.radians(R2))-blade_radius
        R1_Y_1 = (reserved + blade_radius) * math.cos(math.radians(R2))-blade_radius
        #第二刀
        R1_X_03 = (reserved-0.7 + blade_radius) * math.sin(math.radians(R2))-blade_radius
        R1_Y_03 = (reserved-0.7 + blade_radius) * math.cos(math.radians(R2))-blade_radius
        #第三刀
        R1_X_0 = (blade_radius) * math.sin(math.radians(R2))-blade_radius
        R1_Y_0 = (blade_radius) * math.cos(math.radians(R2))-blade_radius

        return R1_X, R1_Y, X2,R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0

    # 11. 计算 R3
    def angles_R3(Y, B, C, angles_BDE, AAY,reserved, blade_radius):
        angles_BX_rad = math.acos((Y**2 + B**2 - C**2) / (2 * Y * B))
        angles_BX = math.degrees(angles_BX_rad)
        X3 = 90 - (AAY + (angles_BX - angles_BDE))
        R3_X = A * math.cos(math.radians(X3))
        R3_Y = A * math.sin(math.radians(X3))

        #第一刀
        R3_X_1 = (reserved + blade_radius) * math.cos(math.radians(X3))-blade_radius
        R3_Y_1 = (reserved + blade_radius) * math.sin(math.radians(X3))+blade_radius

        #第二刀
        R3_X_03 = (reserved-0.7 + blade_radius) * math.cos(math.radians(X3))-blade_radius
        R3_Y_03 = (reserved-0.7 + blade_radius) * math.sin(math.radians(X3))+blade_radius

        #第三刀
        R3_X_0 = (blade_radius) * math.cos(math.radians(X3))-blade_radius
        R3_Y_0 = (blade_radius) * math.sin(math.radians(X3))+blade_radius

        return angles_BX, X3, R3_X, R3_Y , R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0

    # 12. 计算 R4
    def angles_R4(angles_AA,Y, angles_BX, angles_BDE,reserved, blade_radius):
        X4 = angles_BX - angles_BDE
        R4_X = Y * math.sin(math.radians(X4))
        R4_Y = Y * math.cos(math.radians(X4))
        R4 = 180-((90-X4)+angles_BX+angles_AA)

        #第一刀
        R4_X_1 = (reserved + blade_radius) * math.cos(math.radians(R4))-blade_radius
        R4_Y_1 = (reserved + blade_radius) * math.sin(math.radians(R4))-blade_radius
        #第二刀
        R4_X_03 = (reserved-0.7 + blade_radius) * math.cos(math.radians(R4))-blade_radius
        R4_Y_03 = (reserved-0.7 + blade_radius) * math.sin(math.radians(R4))-blade_radius
        #第三刀
        R4_X_0 = (blade_radius) * math.cos(math.radians(R4))-blade_radius
        R4_Y_0 = (blade_radius) * math.sin(math.radians(R4))-blade_radius

        return R4_X, R4_Y ,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0, R4,X4
    
    #13 計算第一個油溝的座標
    def oil_1_all(R1_X, R1_Y,R2_X, R2_Y,  R3_X, R3_Y,R4_X, R4_Y, R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0,R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0,F):
        #第一個油溝的R角第一點座標
        oil_R5_Z_1=F-R1_X-R1_X_1
        oil_R5_X_1=(oil_Z1+R1_Y-R1_Y_1)*2

        oil_R5_Z_03=F-R1_X-R1_X_03
        oil_R5_X_03=(oil_Z1+R1_Y-R1_Y_03)*2

        oil_R5_Z_0=F-R1_X-R1_X_0
        oil_R5_X_0=(oil_Z1+R1_Y-R1_Y_0)*2

        #第一個油溝的R角第二點座標
        oil_R6_Z_1=F-R2_X+R2_X_1
        oil_R6_X_1=(oil_Z1+R2_Y-R2_Y_1)*2

        oil_R6_Z_03=F-R2_X+R2_X_03
        oil_R6_X_03=(oil_Z1+R2_Y-R2_Y_03)*2

        oil_R6_Z_0=F-R2_X+R2_X_0
        oil_R6_X_0=(oil_Z1+R2_Y-R2_Y_0)*2

        #第一個油溝的R角第三點座標
        oil_R7_Z_1=F + R3_X - R3_X_1
        oil_R7_X_1=(oil_Z1 - R3_Y + R3_Y_1)*2

        oil_R7_Z_03=F + R3_X - R3_X_03
        oil_R7_X_03=(oil_Z1 - R3_Y + R3_Y_03)*2

        oil_R7_Z_0=F + R3_X - R3_X_0
        oil_R7_X_0=(oil_Z1 - R3_Y + R3_Y_0)*2


        #第一個油溝的R角第三點座標
        oil_R8_Z_1=F + R4_X - R4_X_1
        oil_R8_X_1=(oil_Z1 - R4_Y - R4_Y_1)*2

        oil_R8_Z_03=F + R4_X - R4_X_03
        oil_R8_X_03=(oil_Z1 - R4_Y - R4_Y_03)*2

        oil_R8_Z_0=F + R4_X - R4_X_0
        oil_R8_X_0=(oil_Z1 - R4_Y - R4_Y_0)*2

        return oil_R5_Z_1, oil_R5_X_1, oil_R6_Z_1, oil_R6_X_1, oil_R7_Z_1, oil_R7_X_1, oil_R8_Z_1, oil_R8_X_1, \
           oil_R5_Z_03, oil_R5_X_03, oil_R6_Z_03, oil_R6_X_03, oil_R7_Z_03, oil_R7_X_03, oil_R8_Z_03, oil_R8_X_03, \
           oil_R5_Z_0, oil_R5_X_0, oil_R6_Z_0, oil_R6_X_0, oil_R7_Z_0, oil_R7_X_0, oil_R8_Z_0, oil_R8_X_0


        





    # 调用各个函数
    angles_ABC = calculate_angles_ABC(A, B, C)
    angles_BDE ,oil_Z1= calculate_angles_BDE(B, D, F)
    A1, A2 = angles_ACD(A, angles_ABC[2], angles_BDE)
    angles_AA = AABB1A(A, B, C)
    X = calculate_X(B, angles_AA)
    Y = calculate_Y(C, B, angles_AA)
    Z  = angles_XY(X, Y)
    AAY = angles_AAY(A, Y)
    R2_X, R2_Y, X1, AAX,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0= angles_R2(angles_BDE, angles_AA, Z, AAY, A, reserved, blade_radius)
    R1_X, R1_Y, X2,R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0 = angles_R1(Y, AAY, X1, Z, reserved, blade_radius)
    angles_BX, X3, R3_X, R3_Y , R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0 = angles_R3(Y, B, C, angles_BDE, AAY,reserved, blade_radius)
    R4_X, R4_Y ,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0, R4,X4= angles_R4(angles_AA,Y, angles_BX, angles_BDE,reserved, blade_radius)

    oil_R5_Z_1,oil_R5_X_1 , oil_R6_Z_1,oil_R6_X_1 , oil_R7_Z_1,oil_R7_X_1 , oil_R8_Z_1,oil_R8_X_1 , oil_R5_Z_03,oil_R5_X_03 , oil_R6_Z_03,oil_R6_X_03 , oil_R7_Z_03,oil_R7_X_03 , oil_R8_Z_03,oil_R8_X_03 , oil_R5_Z_0,oil_R5_X_0 , oil_R6_Z_0,oil_R6_X_0 , oil_R7_Z_0,oil_R7_X_0 , oil_R8_Z_0,oil_R8_X_0=oil_1_all(R1_X, R1_Y,R2_X, R2_Y,  R3_X, R3_Y,R4_X, R4_Y, R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0,R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0,F)
    #print(f"油溝1: {oil_R5_X_1:.2f},{oil_R5_Z_1:.2f}")
    #print(f"油溝2: {oil_R6_X_1:.2f},{oil_R6_Z_1:.2f}")
    #print(f"油溝3: {oil_R7_X_1:.2f},{oil_R7_Z_1:.2f}")
    #print(f"油溝4: {oil_R8_X_1:.2f},{oil_R8_Z_1:.2f}")

    #print(f"油溝1: {oil_R5_X_03:.2f},{oil_R5_Z_03:.2f}")
    #print(f"油溝2: {oil_R6_X_03:.2f},{oil_R6_Z_03:.2f}")
    #print(f"油溝3: {oil_R7_X_03:.2f},{oil_R7_Z_03:.2f}")
    #print(f"油溝4: {oil_R8_X_03:.2f},{oil_R8_Z_03:.2f}")

    #print(f"油溝1: {oil_R5_X_0:.2f},{oil_R5_Z_0:.2f}")
    #print(f"油溝2: {oil_R6_X_0:.2f},{oil_R6_Z_0:.2f}")
    #print(f"油溝3: {oil_R7_X_0:.2f},{oil_R7_Z_0:.2f}")
    #print(f"油溝4: {oil_R8_X_0:.2f},{oil_R8_Z_0:.2f}")

    oil_R5_Z_1, oil_R5_X_1, oil_R6_Z_1, oil_R6_X_1, oil_R7_Z_1, oil_R7_X_1, oil_R8_Z_1, oil_R8_X_1, \
    oil_R5_Z_03, oil_R5_X_03, oil_R6_Z_03, oil_R6_X_03, oil_R7_Z_03, oil_R7_X_03, oil_R8_Z_03, oil_R8_X_03, \
    oil_R5_Z_0, oil_R5_X_0, oil_R6_Z_0, oil_R6_X_0, oil_R7_Z_0, oil_R7_X_0, oil_R8_Z_0, oil_R8_X_0=oil_1_all(R1_X, R1_Y,R2_X, R2_Y,  R3_X, R3_Y,R4_X, R4_Y, R1_X_1,R1_Y_1,R1_X_03,R1_Y_03,R1_X_0,R1_Y_0,R2_X_1,R2_Y_1,R2_X_03,R2_Y_03,R2_X_0,R2_Y_0,R3_X_1,R3_Y_1,R3_X_03,R3_Y_03,R3_X_0,R3_Y_0,R4_X_1,R4_Y_1,R4_X_03,R4_Y_03,R4_X_0,R4_Y_0,F)

    return oil_R5_Z_1, oil_R5_X_1, oil_R6_Z_1, oil_R6_X_1, oil_R7_Z_1, oil_R7_X_1, oil_R8_Z_1, oil_R8_X_1, \
    oil_R5_Z_03, oil_R5_X_03, oil_R6_Z_03, oil_R6_X_03, oil_R7_Z_03, oil_R7_X_03, oil_R8_Z_03, oil_R8_X_03, \
    oil_R5_Z_0, oil_R5_X_0, oil_R6_Z_0, oil_R6_X_0, oil_R7_Z_0, oil_R7_X_0, oil_R8_Z_0, oil_R8_X_0


oil_R5_Z_1, oil_R5_X_1, oil_R6_Z_1, oil_R6_X_1, oil_R7_Z_1, oil_R7_X_1, oil_R8_Z_1, oil_R8_X_1, \
    oil_R5_Z_03, oil_R5_X_03, oil_R6_Z_03, oil_R6_X_03, oil_R7_Z_03, oil_R7_X_03, oil_R8_Z_03, oil_R8_X_03, \
    oil_R5_Z_0, oil_R5_X_0, oil_R6_Z_0, oil_R6_X_0, oil_R7_Z_0, oil_R7_X_0, oil_R8_Z_0, oil_R8_X_0=calculate_all_2(A, B, C, D, F, reserved, blade_radius)

#print(oil_R5_Z_1)


#test1

def calculate_all_3(A , B , D, C , G , H , I , J, K , L , blade_radius):
    def AABB1A(C, G, H):
        # 计算三角形的角度（单位：度）
        angles_CH_rad = math.acos((C**2 + H**2 - G**2) / (2 * C * H))
        angles_GH_rad = math.acos((G**2 + H**2 - C**2) / (2 * G * H))
        angles_CG_rad = math.acos((C**2 + G**2 - H**2) / (2 * C * G))

        angles_CH = math.degrees(angles_CH_rad)
        angles_GH = math.degrees(angles_GH_rad)
        angles_CG = math.degrees(angles_CG_rad)

        print(f"C: {C}")
        #print(f"G: {G}")
        #print(f"H: {H}")    

        return angles_CH, angles_GH, angles_CG

    def calculate_R1_Y(D, H):
        # 计算 R1_Y 和 HR1_Y
        if H <= D:
            raise ValueError("H 必须大于 D")
        
        R1_Y = math.sqrt(H**2 - D**2)
        HR1_Y_rad = math.asin(D / H)
        HR1_Y = math.degrees(HR1_Y_rad)


        return R1_Y, HR1_Y

    
    def calculate_R2_XY(angles_CH,HR1_Y,G):
        GG=90-HR1_Y-angles_CH

        GG_rad = math.radians(GG)#角度轉弧度

        other_G = math.sqrt(G**2 + G**2 - 2*G*G*math.cos(GG_rad))

        R2_X = other_G * math.sin(math.radians(90-((180-GG)/2)))
        R2_Y = other_G * math.cos(math.radians(90-((180-GG)/2)))

        return R2_X,R2_Y,GG
    
    def calculate_R3_XY(C,J,L):
        LJ1 = math.asin(L/J)
        angle_LJ = math.degrees(LJ1)

        R3_X = C * math.cos(math.radians(angle_LJ))
        R3_Y = C * math.sin(math.radians(angle_LJ))

        return R3_X,R3_Y,angle_LJ
    
    def calculate_R4_XY(J,I,angle_LJ):

        II = 90-angle_LJ


        II_rad = math.radians(II)

        other_I = math.sqrt(I**2 + I**2 - 2*I*I*math.cos(II_rad))

        R4_X = R3_X+(other_I * math.sin(math.radians(180-II-((180-II)/2))))

        R4_Z = math.sqrt(R4_X**2+(K/2)**2)

        R4_XY_rad = math.acos(( R4_Z **2 +  R4_X**2 - (K/2)**2) / (2 * R4_Z *  R4_X))
        angles_R4_XY = math.degrees(R4_XY_rad)





        return R4_X , II_rad , angles_R4_XY , R4_Z
    
    def ball_all(C,K,D,R1_Y,GG,angle_LJ,R4_X,reserved1,blade_radius):

        

        angle_R2 = 90-GG

        
        offset_25 = reserved1 + blade_radius
        offset_10 = reserved1 + blade_radius - 1.5  
        offset_03 = reserved1 + blade_radius - 2.2
        offset_01 = reserved1 + blade_radius - 2.4
        offset_00 = blade_radius

        #R1

        starting_point_X_25 = D-(D-offset_25+blade_radius)
        starting_point_X_10 = D-(D-offset_10+blade_radius)
        starting_point_X_03 = D-(D-offset_03+blade_radius)
        starting_point_X_01 = D-(D-offset_01+blade_radius)
        starting_point_X_00 = D-(D)

        starting_point_Y = (R1_Y+blade_radius)*2

        #R2  算出來就有正負號

        R2_X_25 = D-((C-offset_25) * math.sin(math.radians(angle_R2))+blade_radius)
        R2_X_10 = D-((C-offset_10) * math.sin(math.radians(angle_R2))+blade_radius)
        R2_X_03 = D-((C-offset_03) * math.sin(math.radians(angle_R2))+blade_radius)
        R2_X_01 = D-((C-offset_01) * math.sin(math.radians(angle_R2))+blade_radius)
        R2_X_00 = D-((C-offset_00) * math.sin(math.radians(angle_R2))+blade_radius)

        R2_Y_25 = ((C-offset_25) * math.cos(math.radians(angle_R2))+blade_radius)*2
        R2_Y_10 = ((C-offset_10) * math.cos(math.radians(angle_R2))+blade_radius)*2
        R2_Y_03 = ((C-offset_03) * math.cos(math.radians(angle_R2))+blade_radius)*2
        R2_Y_01 = ((C-offset_01) * math.cos(math.radians(angle_R2))+blade_radius)*2
        R2_Y_00 = ((C-offset_00) * math.cos(math.radians(angle_R2))+blade_radius)*2



        
        ARC_25 = C-2.5-blade_radius
        ARC_10 = C-1-blade_radius
        ARC_03 = C-0.3-blade_radius
        ARC_01 = C-0.1-blade_radius
        ARC_00 = C-blade_radius

        #rough

        KY=(K-5)/2-blade_radius

        rough_finish_Y = ((K-5)/2-blade_radius+blade_radius)*2
        rough_X_25 = D-(math.sqrt((C-offset_25)**2 - KY**2)+blade_radius)
        rough_X_10 = D-(math.sqrt((C-offset_10)**2 - KY**2)+blade_radius)
        rough_X_03 = D-(math.sqrt((C-offset_03)**2 - KY**2)+blade_radius)

        #R3

        R3_X_01 = D-((C-offset_01) * math.cos(math.radians(angle_LJ))+blade_radius)
        R3_X_00 = D-((C-offset_00) * math.cos(math.radians(angle_LJ))+blade_radius)

        R3_Y_01 = ((C-offset_01) * math.sin(math.radians(angle_LJ))+blade_radius)*2
        R3_Y_00 = ((C-offset_00) * math.sin(math.radians(angle_LJ))+blade_radius)*2

        #R4

        finish_point_X = D-(R4_X)-blade_radius

        R4_Y_01 = K-0.2
        R4_Y_00 = K


        return starting_point_X_25,starting_point_X_10,starting_point_X_03,starting_point_X_01,starting_point_X_00,starting_point_Y,\
        R2_X_25,R2_X_10,R2_X_03,R2_X_01,R2_X_00,\
        R2_Y_25,R2_Y_10,R2_Y_03,R2_Y_01,R2_Y_00,\
        rough_X_25,rough_X_10,rough_X_03,rough_finish_Y,\
        R3_X_01,R3_X_00,R3_Y_01,R3_Y_00,\
        R4_Y_01,R4_Y_00,finish_point_X,\
        ARC_25,ARC_10,ARC_03,ARC_01,ARC_00
    

    angles_CH, angles_GH, angles_CG = AABB1A(C, G, H)
    R1_Y, HR1_Y = calculate_R1_Y(D, H)
    R2_X,R2_Y ,GG= calculate_R2_XY(angles_CH,HR1_Y,G)
    R3_X,R3_Y,angle_LJ = calculate_R3_XY(C,J,L)
    R4_X , II_rad , angles_R4_XY,R4_Z= calculate_R4_XY(J,I,angle_LJ)
    starting_point_X_25,starting_point_X_10,starting_point_X_03,starting_point_X_01,starting_point_X_00,starting_point_Y,\
        R2_X_25,R2_X_10,R2_X_03,R2_X_01,R2_X_00,\
        R2_Y_25,R2_Y_10,R2_Y_03,R2_Y_01,R2_Y_00,\
        rough_X_25,rough_X_10,rough_X_03,rough_finish_Y,\
        R3_X_01,R3_X_00,R3_Y_01,R3_Y_00,\
        R4_Y_01,R4_Y_00,finish_point_X , \
        ARC_25,ARC_10,ARC_03,ARC_01,ARC_00 = ball_all(C,K,D,R1_Y,GG,angle_LJ,R4_X,reserved1,blade_radius)



    # 打印结果
    #print(f"角度 CH: {angles_CH:.2f}")
    #print(f"角度 GH: {angles_GH:.2f}")
    #print(f"角度 CG: {angles_CG:.2f}")

    #print(f"R1_Y: {R1_Y:.2f}")
    #print(f"HR1_Y (弧度): {HR1_Y:.2f}")

    #print(f"R2_X: {R2_X:.2f}")
    #print(f"R2_Y: {R2_Y:.2f}")

    #print(f"R3_X: {R3_X:.2f}")
    #print(f"R3_Y: {R3_Y:.2f}")

    #print(f"R4_X: {R4_X:.2f}")

    #print(f"測試: {R2_X_00:.2f}")
    #print(f"測試: {R2_Y_00:.2f}")



    return starting_point_X_25,starting_point_X_10,starting_point_X_03,starting_point_X_01,starting_point_X_00,starting_point_Y,\
        R2_X_25,R2_X_10,R2_X_03,R2_X_01,R2_X_00,\
        R2_Y_25,R2_Y_10,R2_Y_03,R2_Y_01,R2_Y_00,\
        rough_X_25,rough_X_10,rough_X_03,rough_finish_Y,\
        R3_X_01,R3_X_00,R3_Y_01,R3_Y_00,\
        R4_Y_01,R4_Y_00,finish_point_X,\
        ARC_25,ARC_10,ARC_03,ARC_01,ARC_00


starting_point_X_25,starting_point_X_10,starting_point_X_03,starting_point_X_01,starting_point_X_00,starting_point_Y,\
        R2_X_25,R2_X_10,R2_X_03,R2_X_01,R2_X_00,\
        R2_Y_25,R2_Y_10,R2_Y_03,R2_Y_01,R2_Y_00,\
        rough_X_25,rough_X_10,rough_X_03,rough_finish_Y,\
        R3_X_01,R3_X_00,R3_Y_01,R3_Y_00,\
        R4_Y_01,R4_Y_00,finish_point_X , \
        ARC_25,ARC_10,ARC_03,ARC_01,ARC_00=calculate_all_3(A , B , D, C , G , H , I , J, K , L , blade_radius)
                          
    




    #return angles_CH,angles_GH,angles_CG,R1_Y,HR1_Y  
   


#angles_CH,angles_GH,angles_CG,R1_Y,HR1_Y =calculate_all_3(C,D,G,H,I,blade_radius)

#print(f"{angles_CH:.2f}")
#print(f"{angles_GH:.2f}")
#print(f"{angles_CG:.2f}")



















def A123 (A,B,C):
    def A456(A,B,C):
        X=A+B
        Y=A+C

        return X , Y
    X,Y=A456(A,B,C)
    return X ,Y

X , Y=A123 (A,B,C)

#print(X)
#print(Y)


#root.mainloop()




    
