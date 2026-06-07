import pygame
import math
import sys

pygame.init()

# 窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("跳动爱心")
clock = pygame.time.Clock()

# 颜色
RED = (255, 50, 50)
PINK = (255, 105, 180)
WHITE = (255, 255, 255)

def heart_points(center_x, center_y, size, t):
    """生成心形点集，t为跳动时间参数"""
    points = []
    scale = size * (0.9 + 0.1 * math.sin(t * 8))  # 跳动效果
    for theta in range(0, 360, 2):
        rad = math.radians(theta)
        # 心形参数方程
        x = 16 * math.sin(rad) ** 3
        y = 13 * math.cos(rad) - 5 * math.cos(2*rad) - 2*math.cos(3*rad) - math.cos(4*rad)
        points.append((center_x + x * scale, center_y - y * scale))
    return points

def draw_glow(surface, color, center, size, t):
    """绘制发光爱心"""
    glow_size = size + 8
    for i in range(5):
        alpha = 30 - i * 5
        s = size + (5 - i) * 2
        points = heart_points(center[0], center[1], s * 0.8, t)
        if len(points) > 2:
            pygame.draw.polygon(surface, (*color, alpha), points, 0)
    
    # 主体爱心
    points = heart_points(center[0], center[1], size * 0.8, t)
    pygame.draw.polygon(surface, color, points, 0)

# 粒子效果
particles = []

running = True
time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    
    # 背景星空效果
    for _ in range(5):
        import random
        pygame.draw.circle(screen, (255,255,200), 
                          (random.randint(0,WIDTH), random.randint(0,HEIGHT)), 1)
    
    # 主爱心
    time += 0.016  # 约60fps
    center = (WIDTH//2, HEIGHT//2)
    size = 12
    
    draw_glow(screen, RED, center, size, time)
    
    # 添加漂浮粒子
    import random
    if random.random() < 0.3:
        particles.append({
            'x': WIDTH//2 + random.randint(-50,50),
            'y': HEIGHT//2 + random.randint(-50,50),
            'vx': random.uniform(-1,1),
            'vy': random.uniform(-2,0),
            'life': 60
        })
    
    for p in particles[:]:
        p['x'] += p['vx']
        p['y'] += p['vy']
        p['life'] -= 1
        pygame.draw.circle(screen, PINK, (int(p['x']), int(p['y'])), 2)
        if p['life'] <= 0:
            particles.remove(p)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()