# Pygame Learning & Integration Task List

## Phase 1: Pygame Fundamentals
### 1. Pygame Setup & Window Management
- [ ] Install pygame (`pip install pygame`)
- [ ] Learn to create a pygame window with `pygame.init()` and `pygame.display.set_mode()`
- [ ] Understand the main game loop and event handling
- [ ] Learn about `pygame.event.get()` and handling `pygame.QUIT`
- [ ] Learn frame rate control with `pygame.time.Clock()` and `tick()`

### 2. Basic Drawing & Colors
- [ ] Understand color representation in pygame (RGB tuples)
- [ ] Learn to draw rectangles with `pygame.draw.rect()`
- [ ] Learn to draw circles with `pygame.draw.circle()`
- [ ] Learn to draw lines with `pygame.draw.line()`
- [ ] Understand `pygame.display.flip()` or `pygame.display.update()`
- [ ] Learn background clearing with `surface.fill()`

### 3. Fonts & Text Rendering
- [ ] Learn `pygame.font.Font()` or `pygame.font.SysFont()`
- [ ] Render text with `font.render()`
- [ ] Display text on screen by blitting surfaces

## Phase 2: Data Structure Understanding
### 4. Map Coordinate System
- [ ] Understand how zones have (x, y) coordinates from the map file
- [ ] Learn to calculate screen positions from map coordinates (scaling/translation)
- [ ] Understand zone properties: name, position, max_drones, zone_type, color

### 5. Zone & Connection Visualization
- [ ] Understand zone types: normal, restricted (2-turn), priority, blocked
- [ ] Learn how to visually differentiate zones (colors, patterns, borders)
- [ ] Understand connections between zones (edges in the graph)
- [ ] Learn how to draw connections as lines between zones

### 6. Drone State & Movement
- [ ] Understand `SimDrone` object: current_zone, path, path_index, in_transit_connection, target_zone, turns_left, delivered
- [ ] Understand drone movement: zone→transit→zone (2 turns for restricted zones)
- [ ] Learn to track drone position during animation

## Phase 3: Pygame Implementation
### 7. Creating the Visualization System
- [ ] Design a `PygameRenderer` class to handle all drawing
- [ ] Create methods for: drawing zones, drawing connections, drawing drones
- [ ] Implement coordinate scaling (map coords → screen pixels)
- [ ] Add zoom and pan capabilities (optional but useful)

### 8. Zone Rendering
- [ ] Draw zones as circles or rectangles at (x, y) positions
- [ ] Color code zones: normal (blue), restricted (red), priority (green), blocked (gray), start/end hubs (special colors)
- [ ] Draw zone names/labels inside zones
- [ ] Show drone count inside each zone
- [ ] Draw zone capacity indicators (e.g., "2/3 drones")

### 9. Connection Rendering
- [ ] Draw lines between connected zones
- [ ] Color code connection lines based on capacity
- [ ] Show connection capacity info (e.g., "1/2 drones in transit")
- [ ] Animate drones moving along connections

### 10. Drone Rendering & Animation
- [ ] Draw drones as small circles or dots with unique colors/IDs
- [ ] Show drone ID (D1, D2, etc.) on each drone
- [ ] Animate drone movement smoothly between zones (not instant jumps)
- [ ] Color code drones by state (active, in_transit, delivered)
- [ ] Smooth animation between zones using interpolation (linear or easing)

## Phase 4: Turn-by-Turn Simulation
### 11. Pause/Play/Step Controls
- [ ] Add keyboard controls: SPACE to pause/play, ARROW keys to step forward/backward
- [ ] Display current turn number on screen
- [ ] Show simulation status (running/paused)

### 12. Simulation Loop Integration
- [ ] Modify `main.py` to use pygame instead of terminal output
- [ ] Call simulator one turn at a time (or collect all turns upfront)
- [ ] Update pygame display each turn
- [ ] Add FPS/speed control (slow down to see movement)

### 13. Timeline & History
- [ ] Keep track of all turns and drone states
- [ ] Allow stepping forward/backward through turns
- [ ] Display turn history or summary
- [ ] Show which drones have been delivered

## Phase 5: Polish & Features
### 14. HUD (Heads-Up Display)
- [ ] Display turn counter at top
- [ ] Show active drones vs delivered drones
- [ ] Show simulation speed/FPS
- [ ] Display map name and stats
- [ ] Show legend (zone types, colors)

### 15. Debugging Visualization
- [ ] Highlight selected drone or zone
- [ ] Show drone path (complete path from start to end)
- [ ] Show active connection capacity usage
- [ ] Display zone capacity usage visually

### 16. Mouse Interaction (Optional)
- [ ] Click on drones to highlight their path
- [ ] Click on zones to see occupancy details
- [ ] Display tooltips with zone/drone info

## Phase 6: Optimization & Testing
### 17. Performance
- [ ] Ensure smooth rendering at 60 FPS
- [ ] Handle large maps (many zones/drones)
- [ ] Optimize drawing operations

### 18. Testing
- [ ] Test with all map files (easy, medium, hard)
- [ ] Verify drone paths are correct
- [ ] Check zone/connection capacity constraints visually
- [ ] Test all zone types (restricted, priority, blocked)

---

## Key Pygame Resources
- Official docs: https://www.pygame.org/docs/
- Surfaces: Everything drawable is a Surface
- Event loop: Handle quit, keyboard, mouse
- Drawing primitives: rect, circle, line, polygon
- Transforms: rotate, scale surfaces
- Animation: Use dt (delta time) or frame counters

## Integration Checklist
- [ ] Remove `_render_grid()` method from `simulation.py`
- [ ] Remove visual output from `main.py`
- [ ] Remove `visual_frames` from simulation return value
- [ ] Create new `pygame_main.py` or modify `main.py` to use pygame
- [ ] Create `PygameRenderer` class in new file
- [ ] Add pygame dependency to requirements/setup
- [ ] Test with sample maps

## Important Notes
- Pygame runs its own event loop, different from terminal input
- Surfaces need to be updated/flipped after drawing
- Use `pygame.time.Clock()` to control frame rate
- Consider creating a separate rendering layer from simulation logic
- Drone animation should be smooth: interpolate position between turns, don't jump
