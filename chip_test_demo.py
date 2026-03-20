import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
import numpy as np

# 🎯 CHIP TESTING DEMO - See the Power of Computing! 🎯
print("=" * 60)
print("🔬 MICROCHIP STRESS TEST SIMULATOR 🔬")
print("=" * 60)
print("\n💡 Did you know? Every smartphone, computer, and game console")
print("   has chips that must be tested under extreme conditions!")
print("\n🌡️  We're testing chips at different temperatures...")
print("   Let's see how powerful computers are at running tests!\n")

# Choose mode: LIVE or FAST
print("Choose your demo mode:")
print("1. 🎬 LIVE MODE - Watch tests appear in real-time (animated!)")
print("2. ⚡ FAST MODE - Run all tests instantly and see final results")
mode = input("\nEnter 1 or 2: ").strip()

if mode == "1":
    LIVE_MODE = True
    NUM_TESTS = 1000  # Fewer tests for live animation
else:
    LIVE_MODE = False
    NUM_TESTS = 50000  # 50,000 tests - imagine doing this by hand! 🚀

temperatures = []
voltages = []
results = []
test_times = []

print(f"🚀 Running {NUM_TESTS:,} tests... Watch how fast computers work!\n")

start_time = time.time()

if LIVE_MODE:
    print("🎬 LIVE MODE: Watch the magic happen in real-time!\n")
    print("🟢 Green dots = PASS   🔴 Red dots = FAIL\n")
    
    # Collect data first
    temperatures = []
    voltages = []
    results = []
    
    for i in range(NUM_TESTS):
        temp = random.uniform(20, 100)
        voltage = random.uniform(0.9, 1.3)
        
        fail_probability = 0
        if temp > 80:
            fail_probability += (temp - 80) * 0.02
        if voltage > 1.2:
            fail_probability += (voltage - 1.2) * 0.5
        
        test_result = "PASS" if random.random() > fail_probability else "FAIL"
        
        temperatures.append(temp)
        voltages.append(voltage)
        results.append(test_result)
    
    # Create animated visualization
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle('🎬 LIVE: Watch Tests Running in Real-Time! 🎬', fontsize=16, fontweight='bold')
    
    ax.set_xlim(15, 105)
    ax.set_ylim(0.85, 1.35)
    ax.set_xlabel('Temperature (°C)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Voltage (V)', fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Add danger zones
    ax.axvline(x=80, color='orange', linestyle='--', linewidth=2, alpha=0.5, label='High Temp Zone')
    ax.axhline(y=1.2, color='purple', linestyle='--', linewidth=2, alpha=0.5, label='High Voltage Zone')
    
    # Counter text
    counter_text = ax.text(0.02, 0.98, '', transform=ax.transAxes, 
                          fontsize=14, fontweight='bold',
                          verticalalignment='top',
                          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Store plot objects
    pass_points = ax.scatter([], [], c='green', s=50, alpha=0.6, label='✅ PASS')
    fail_points = ax.scatter([], [], c='red', s=50, alpha=0.6, label='❌ FAIL')
    ax.legend(loc='upper right', fontsize=12)
    
    # Animation data
    pass_temps = []
    pass_volts = []
    fail_temps = []
    fail_volts = []
    
    def init():
        pass_points.set_offsets(np.empty((0, 2)))
        fail_points.set_offsets(np.empty((0, 2)))
        counter_text.set_text('')
        return pass_points, fail_points, counter_text
    
    def animate(frame):
        if frame < len(temperatures):
            if results[frame] == "PASS":
                pass_temps.append(temperatures[frame])
                pass_volts.append(voltages[frame])
            else:
                fail_temps.append(temperatures[frame])
                fail_volts.append(voltages[frame])
            
            # Update scatter plots
            if pass_temps:
                pass_points.set_offsets(np.column_stack([pass_temps, pass_volts]))
            if fail_temps:
                fail_points.set_offsets(np.column_stack([fail_temps, fail_volts]))
            
            # Update counter
            passed = len(pass_temps)
            failed = len(fail_temps)
            total = passed + failed
            counter_text.set_text(f'Tests: {total:,}/{NUM_TESTS:,}\n✅ Pass: {passed:,}\n❌ Fail: {failed:,}')
        
        return pass_points, fail_points, counter_text
    
    # Create animation (show every 10th frame for speed)
    frames_to_show = list(range(0, NUM_TESTS, max(1, NUM_TESTS // 100)))  # Show 100 frames
    anim = animation.FuncAnimation(fig, animate, init_func=init, 
                                   frames=frames_to_show, 
                                   interval=50, blit=True, repeat=False)
    
    elapsed_time = time.time() - start_time
    total_tests = len(results)
    passed = results.count("PASS")
    failed = results.count("FAIL")
    pass_rate = (passed / total_tests) * 100
    
    print("✨ Animation ready! Close the window when done watching.\n")
    plt.show()
    
else:
    # FAST MODE - Original code
    temperatures = []
    voltages = []
    results = []
    test_times = []
    
    # Simulate realistic chip testing with random variations
    for i in range(NUM_TESTS):
        # Random temperature between 20°C and 100°C
        temp = random.uniform(20, 100)
        
        # Random voltage between 0.9V and 1.3V
        voltage = random.uniform(0.9, 1.3)
        
        # Simulate test result (chips fail more at high temp/voltage)
        fail_probability = 0
        if temp > 80:
            fail_probability += (temp - 80) * 0.02
        if voltage > 1.2:
            fail_probability += (voltage - 1.2) * 0.5
        
        test_result = "PASS" if random.random() > fail_probability else "FAIL"
        
        temperatures.append(temp)
        voltages.append(voltage)
        results.append(test_result)
        test_times.append(time.time() - start_time)
        
        # Show progress every 10,000 tests
        if (i + 1) % 10000 == 0:
            elapsed = time.time() - start_time
            tests_per_sec = (i + 1) / elapsed
            print(f"✓ {i+1:,} tests completed in {elapsed:.2f}s ({tests_per_sec:.0f} tests/second)")

    elapsed_time = time.time() - start_time

    # Calculate statistics
    total_tests = len(results)
    passed = results.count("PASS")
    failed = results.count("FAIL")
    pass_rate = (passed / total_tests) * 100

    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    print(f"⏱️  Total time: {elapsed_time:.2f} seconds")
    print(f"⚡ Speed: {total_tests/elapsed_time:.0f} tests per second")
    print(f"📈 Total tests: {total_tests:,}")
    print(f"✅ Passed: {passed:,} ({pass_rate:.1f}%)")
    print(f"❌ Failed: {failed:,} ({100-pass_rate:.1f}%)")
    print("\n💪 That's the POWER of computing! Could you test")
    print(f"   {total_tests:,} chips by hand in {elapsed_time:.1f} seconds? ")

    # Create impressive visualizations with subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('🔬 Microchip Testing: The Power of Computing! 🔬', fontsize=16, fontweight='bold')

    # Color code: Green for PASS, Red for FAIL
    colors = ['green' if r == "PASS" else 'red' for r in results]

    # Plot 1: Temperature vs Voltage (showing all tests!)
    # Separate pass and fail for better visualization
    pass_mask = [r == "PASS" for r in results]
    fail_mask = [r == "FAIL" for r in results]
    temp_pass = [t for t, m in zip(temperatures, pass_mask) if m]
    volt_pass = [v for v, m in zip(voltages, pass_mask) if m]
    temp_fail = [t for t, m in zip(temperatures, fail_mask) if m]
    volt_fail = [v for v, m in zip(voltages, fail_mask) if m]
    
    ax1.scatter(temp_pass, volt_pass, c='green', alpha=0.4, s=15, label=f'✅ PASS ({len(temp_pass):,})')
    ax1.scatter(temp_fail, volt_fail, c='red', alpha=0.6, s=20, label=f'❌ FAIL ({len(temp_fail):,})', marker='x')
    ax1.set_xlabel('Temperature (°C)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Voltage (V)', fontsize=11, fontweight='bold')
    ax1.set_title(f'🌡️ All {total_tests:,} Tests: Each Dot = 1 Test!', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper left', fontsize=10)
    # Add text box explaining
    textstr = 'Look for patterns:\n• Green cluster = Safe zone\n• Red spots = Danger zone'
    ax1.text(0.98, 0.02, textstr, transform=ax1.transAxes, fontsize=9,
             verticalalignment='bottom', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Plot 2: Pass/Fail Statistics
    categories = ['PASS', 'FAIL']
    counts = [passed, failed]
    colors_bar = ['#2ecc71', '#e74c3c']
    bars = ax2.bar(categories, counts, color=colors_bar, edgecolor='black', linewidth=2)
    ax2.set_ylabel('Number of Tests', fontsize=11, fontweight='bold')
    ax2.set_title(f'✅ Pass vs Fail ({total_tests:,} tests)', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, max(counts) * 1.2)
    # Add count labels on bars
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                 f'{count:,}\n({count/total_tests*100:.1f}%)',
                 ha='center', va='bottom', fontweight='bold', fontsize=10)

    # Plot 3: Temperature Distribution
    ax3.hist(temperatures, bins=50, color='orange', edgecolor='black', alpha=0.7)
    ax3.axvline(x=80, color='red', linestyle='--', linewidth=2, label='Danger Zone (>80°C)')
    ax3.set_xlabel('Temperature (°C)', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax3.set_title(f'🌡️ Temperature Distribution ({total_tests:,} tests)', fontsize=12, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # Plot 4: Failure Rate by Temperature Range
    temp_ranges = ['20-40°C', '40-60°C', '60-80°C', '80-100°C']
    range_fails = [0, 0, 0, 0]
    range_totals = [0, 0, 0, 0]

    for temp, result in zip(temperatures, results):
        if temp < 40:
            idx = 0
        elif temp < 60:
            idx = 1
        elif temp < 80:
            idx = 2
        else:
            idx = 3
        
        range_totals[idx] += 1
        if result == "FAIL":
            range_fails[idx] += 1

    failure_rates = [(fails/total)*100 if total > 0 else 0 
                     for fails, total in zip(range_fails, range_totals)]

    bars = ax4.bar(temp_ranges, failure_rates, color=['#2ecc71', '#f39c12', '#e67e22', '#e74c3c'],
                   edgecolor='black', linewidth=2)
    ax4.set_ylabel('Failure Rate (%)', fontsize=11, fontweight='bold')
    ax4.set_xlabel('Temperature Range', fontsize=11, fontweight='bold')
    ax4.set_title('🔥 Failure Rate by Temperature', fontsize=12, fontweight='bold')
    ax4.set_ylim(0, max(failure_rates) * 1.2 if max(failure_rates) > 0 else 10)
    ax4.grid(True, alpha=0.3, axis='y')
    # Add percentage labels on bars
    for bar, rate in zip(bars, failure_rates):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                 f'{rate:.1f}%',
                 ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.show()

    print("\n" + "=" * 60)
    print("🌟 WHAT YOU JUST SAW:")
    print("=" * 60)
    print(f"✨ The computer tested {total_tests:,} virtual chips")
    print(f"⚡ At {total_tests/elapsed_time:.0f} tests per second!")
    print("🎨 Created beautiful graphs automatically")
    print("🧮 Calculated all statistics instantly")
    print("\n💡 This is what engineers do with REAL chips!")
    print("   They write code to test millions of chips automatically.")
    print("\n🚀 YOU could be the one writing code like this!")
    print("   Computers + Your Ideas = Unlimited Power! 💪")
    print("=" * 60)
