package _096_UniqueBinarySearchTrees;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.Timeout;

public class SolutionDFSTest {

    /** Test method for {@link _096_UniqueBinarySearchTrees.SolutionDFS } */
    SolutionDFS solution;
    
    @Rule
    public Timeout globalTimeout = new Timeout(200);

    @Before
    public void setUp() throws Exception {
        solution = new SolutionDFS();
    }

    @After
    public void tearDown() throws Exception {
        solution = null;
    }

    @Test
    public void Test1() {
        int n = 3;
        int actual = solution.numTrees(n);
        int expected = 5;
        assertEquals(expected, actual);
    }

    @Test
    public void Test2() {
        int n = 1;
        int actual = solution.numTrees(n);
        int expected = 1;
        assertEquals(expected, actual);
    }

    @Test
    public void Test3() {
        int n = 2;
        int actual = solution.numTrees(n);
        int expected = 2;
        assertEquals(expected, actual);
    }

    // fail test which TLE
    @Test
    public void Test4() {
        int n = 19;
        int actual = solution.numTrees(n);
        int expected = 1767263190;
        assertEquals(expected, actual);
    }

}
