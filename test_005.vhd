
    Library ieee;
    USE ieee.std_logic_vector.all;
    
--    ENTITY MyEntity is

 -- Define the top-level module
 ENTITY top_level is
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
BEGIN

END behavior;
