package com.fss;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        assertTrue( true );
    }
    @Test
    public void testsum(){
        App app = new App();
        int expected= 10;
        int actual= app.testsum();
        assertEquals(expected, actual);
        assertTrue(2<3);
        assertFalse(2>3);
    }
}
