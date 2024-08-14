-- Define the top-level module
ENTITY top_level IS
    PORT (
        clk     : IN  std_logic;
        rst     : IN  std_logic;
        input1  : IN  std_logic_vector(7 DOWNTO 0);
        input2  : IN  std_logic_vector(7 DOWNTO 0);
        output1 : OUT std_logic_vector(7 DOWNTO 0);
        output2 : OUT std_logic_vector(7 DOWNTO 0)
    );
END top_level;

ARCHITECTURE behavior OF top_level IS
    -- Declare internal signals
    SIGNAL internal_signal1 : std_logic_vector(7 DOWNTO 0);
    SIGNAL internal_signal2 : std_logic_vector(7 DOWNTO 0);

    -- Component declarations
    COMPONENT module1
        PORT (
            clk     : IN  std_logic;
            rst     : IN  std_logic;
            data_in : IN  std_logic_vector(7 DOWNTO 0);
            data_out: OUT std_logic_vector(7 DOWNTO 0)
        );
    END COMPONENT;

    COMPONENT module2
        PORT (
            clk     : IN  std_logic;
            rst     : IN  std_logic;
            data_in : IN  std_logic_vector(7 DOWNTO 0);
            data_out: OUT std_logic_vector(7 DOWNTO 0)
        );
    END COMPONENT;

    COMPONENT module3
        PORT (
            clk     : IN  std_logic;
            rst     : IN  std_logic;
            data_in : IN  std_logic_vector(7 DOWNTO 0);
            data_out: OUT std_logic_vector(7 DOWNTO 0)
        );
    END COMPONENT;

    COMPONENT module4
        PORT (
            clk     : IN  std_logic;
            rst     : IN  std_logic;
            data_in : IN  std_logic_vector(7 DOWNTO 0);
            data_out: OUT std_logic_vector(7 DOWNTO 0)
        );
    END COMPONENT;

BEGIN
    -- Instantiate module1
    U1: module1 PORT MAP (
        clk      => clk,
        rst      => rst,
        data_in  => input1,
        data_out => internal_signal1
    );

    -- Instantiate module2
    U2: module2 PORT MAP (
        clk      => clk,
        rst      => rst,
        data_in  => internal_signal1,
        data_out => internal_signal2
    );

    -- Instantiate module3
    U3: module3 PORT MAP (
        clk      => clk,
        rst      => rst,
        data_in  => internal_signal2,
        data_out => output1
    );

    -- Instantiate module4
    U4: module4 PORT MAP (
        clk      => clk,
        rst      => rst,
        data_in  => input2,
        data_out => output2
    );

END behavior;
